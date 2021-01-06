# ros2_text_to_speech

## Installation
```shell
sudo apt install espeak -y
sudo apt install gnustep-gui-runtime
sudo apt install speech-dispatcher
sudo apt install festival festival-doc festvox-kdlpc16k festvox-ellpc11k festvox-italp16k festvox-itapc16k -y
sudo pip3 install gTTS
sudo apt install mpg321
```

## Launch
```shell
ros2 launch ros2_text_to_speech ros2_text_to_speech_launch.py
```

## Shell Example
```shell
ros2 action send_goal /ros2_text_to_speech/tts ros2_text_to_speech_interfaces/action/TTS "{'text': 'Hello'}"
```
