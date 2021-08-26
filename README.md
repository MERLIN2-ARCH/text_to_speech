# TTS (Text To Speech)

## Description

- ROS2 Foxy Fitzroy
- ROS2 text to speech system
- Libs:
  - espeak
  - speech-dispatcher
  - festival
  - gTTS
  - mpg321

## Installation
```shell
cd ~/ros2_foxy/src
git clone text_to_speech
cd text_to_speech
./install_dependencies.sh
```

## Launch
```shell
ros2 launch text_to_speech text_to_speech_launch.py
```

## Shell Example
```shell
ros2 action send_goal /text_to_speech/tts text_to_speech_interfaces/action/TTS "{'text': 'Hello world', 'config': {'volume': '0.5', 'rate': '100', 'language': 'en', 'gender': 'm', 'tool': '1'}}"
```
