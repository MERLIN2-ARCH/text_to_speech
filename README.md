# TTS (Text To Speech)

TTS for ROS 2 with several tools:

- espeak
- speech-dispatcher
- festival
- gTTS
- mpg321

## Installation

```shell
# dependencies
$ sudo apt install espeak -y
$ sudo apt install speech-dispatcher -y
$ sudo apt install festival festival-doc festvox-kdlpc16k festvox-ellpc11k festvox-italp16k festvox-itapc16k -y
$ sudo pip3 install gTTS
$ sudo apt install mpg321 -y

# clone
$ cd ~/ros2_ws/src
$ git clone https://github.com/MERLIN2-ARCH/text_to_speech.git

# colcon
$ cd ~/ros2_ws
$ colcon build
```

## Usage

### Launch

```shell
$ ros2 launch text_to_speech text_to_speech.launch.py
```

### Shell Example

```shell
$ ros2 action send_goal /text_to_speech/tts text_to_speech_interfaces/action/TTS "{'text': 'Hello world', 'config': {'volume': '0.5', 'rate': '100', 'language': 'en', 'gender': 'm', 'tool': '1'}}"
```
