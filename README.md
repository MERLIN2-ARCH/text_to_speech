# ros2_text_to_speech

## Installation
```shell
cd ~/ros2_foxy/src
git clone ros2_text_to_speech
cd ros2_text_to_speech
./install_dependencies.sh
```

## Launch
```shell
ros2 launch ros2_text_to_speech ros2_text_to_speech_launch.py
```

## Shell Example
```shell
ros2 action send_goal /ros2_text_to_speech/tts ros2_text_to_speech_interfaces/action/TTS "{'text': 'Hello world', 'config': {'volume': '0.5', 'rate': '100', 'language': 'en', 'gender': 'm', 'tool': '1'}}"
```
