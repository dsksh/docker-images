#!/usr/bin/env python

import rospy

from niryo_robot_msgs.msg import CommandStatus
from std_msgs.msg import Bool

from niryo_robot_arm_commander.srv import JogShift, JogShiftRequest
from niryo_robot_msgs.srv import SetBool

#from geometry_msgs.msg import Twist

from sensor_msgs.msg import Joy

# Jog callback handler.

op = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

def callback(msg):
    print(msg)
    op[0] = msg.axes[0]
    op[1] = msg.axes[1]
    op[2] = msg.axes[2]
    op[3] = msg.axes[3]

    if msg.buttons[4] == 1:
        op[4] = 1.0
    elif msg.buttons[5] == 1:
        op[4] = -1.0
    else:
        op[4] = 0.0

    if msg.buttons[6] == 1:
        op[5] = 1.0
    elif msg.buttons[7] == 1:
        op[5] = -1.0
    else:
        op[5] = 0.0

# Jog enabled message handler.

jog_enabled = False

def callback_jog_enabled(ros_data):
    jog_enabled = ros_data.data

def set_jog(set_bool):
    if set_bool == jog_enabled:
        return CommandStatus.SUCCESS, "Already enable"
    rospy.wait_for_service('/niryo_robot/jog_interface/enable')
    try:
        enable_service = rospy.ServiceProxy('/niryo_robot/jog_interface/enable', SetBool)
        response = enable_service(True)
    except rospy.ServiceException as e:
        raise Exception("Service call failed: {}".format(e))
    rospy.sleep(0.1)
    return response

# Initializing ROS node
rospy.init_node('ned_joy')

joy_subscriber = rospy.Subscriber('joy', Joy, callback, queue_size=10)

jog_enabled_subscriber = rospy.Subscriber('/niryo_robot/jog_interface/is_enabled',
                                          Bool, 
                                          callback_jog_enabled,
                                          queue_size=1)

set_jog(True)

while not rospy.is_shutdown():
    g = 5
    j0 = g * op[0]
    j1 = g * op[1]
    j2 = g * op[3]
    j3 = -g * op[2]
    j4 = g * op[4]
    j5 = -g * op[5]

    cmd = JogShiftRequest.JOINTS_SHIFT
    #cmd = JogShiftRequest.POSE_SHIFT
    shift_values = [j0, j1, j2, j3, j4, j5]

    init_time = rospy.get_time()
    if not jog_enabled:
        set_jog(True)
    service_name = '/niryo_robot/jog_interface/jog_shift_commander'
    rospy.wait_for_service(service_name)
    try:
        jog_commander_service = rospy.ServiceProxy(service_name, JogShift)
        req = JogShiftRequest()
        req.cmd = cmd
        req.shift_values = shift_values
        response = jog_commander_service(req)
    except rospy.ServiceException as e:
        raise Exception("Service call failed: {}".format(e))
    rospy.sleep(0.15 - (rospy.get_time() - init_time))

    #rospy.sleep(1)

# eof
