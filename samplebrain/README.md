# Samplebrain

[https://gitlab.com/then-try-this/samplebrain](https://gitlab.com/then-try-this/samplebrain)

## How to run on Mac OS

```
$ brew install pulseaudio
$ pulseaudio --load=module-native-protocol-tcp --exit-idle-time=-1 --daemon
$ docker compose run samplebrain
```