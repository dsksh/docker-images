#!/usr/bin/env python

# Imports
import rospy

from niryo_robot_msgs.msg import CommandStatus
from std_msgs.msg import Bool

from niryo_robot_arm_commander.srv import JogShift, JogShiftRequest
from niryo_robot_msgs.srv import SetBool

#from niryo_robot_python_ros_wrapper import *

#import sys
import readchar

# Reference:
# https://docs.niryo.com/applications/ned/v1.0.0/en/source/tutorials/control_ned_ros_node_joystick.html
# https://github.com/NiryoRobotics/ned_ros/tree/v3.2.0/niryo_robot_user_interface/scripts/jog_interface

jog_enabled = False

def callback_subscriber_jog_enabled(ros_data):
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
rospy.init_node('niryo_ned_kbd')

jog_enabled_subscriber = rospy.Subscriber('/niryo_robot/jog_interface/is_enabled',
                                          Bool, 
                                          callback_subscriber_jog_enabled,
                                          queue_size=1)

set_jog(True)

print("k/j: up/down, l/h: right/left, p/n: fwd/bwd")

while not rospy.is_shutdown():
    c = readchar.readchar()
    g = 5
    px = 0.0
    py = 0.0
    pz = 0.0
    if c == 'k':
        py = g
    elif c == 'j':
        py = -g
    elif c == 'l':
        px = -g
    elif c == 'h':
        px = g
    elif c == 'p':
        pz = g
    elif c == 'n':
        pz = -g

    cmd = JogShiftRequest.JOINTS_SHIFT
    #cmd = JogShiftRequest.POSE_SHIFT
    shift_values = [px, py, pz, 0.0, 0.0, 0.0]

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
