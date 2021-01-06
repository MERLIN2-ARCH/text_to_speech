# ros2_text_to_speech

## Installation
```shell
sudo apt update && sudo apt install espeak ffmpeg libespeak1 -y
sudo pip3 install pyttsx3
```

## Launch
```shell
ros2 launch ros2_text_to_speech ros2_text_to_speech_launch.py
```

## Shell Example
```shell
ros2 action send_goal /ros2_text_to_speech/tts ros2_text_to_speech_interfaces/action/TTS "{'text': 'Hello'}"
```
