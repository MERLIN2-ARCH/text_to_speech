
""" Text to Speech for ROS2 """

import os
import pyttsx3
import rclpy
from ros2_text_to_speech_interfaces.action import TTS
from custom_ros2 import (
    Node,
    ActionSingleServer
)


class TtsNode(Node):
    """ TTS Node Class """

    def __init__(self):

        super().__init__('tts_node')

        self.__engine = pyttsx3.init(driverName="espeak")

        # action server
        self.__action_server = ActionSingleServer(self,
                                                  TTS,
                                                  "tts",
                                                  execute_callback=self.__execute_server,
                                                  cancel_callback=self.__cancel_callback
                                                  )

    def destroy(self):
        """ destroy node method """

        self.__action_server.destroy()
        super().destroy_node()

    def __cancel_callback(self):
        os.system("pkill aplay")
        self.__engine.stop()

    def __execute_server(self, goal_handle):
        """ execute action server

        Args:
            goal_handle: goal_handle
        """

        request = goal_handle.request
        result = TTS.Result()

        self.__engine.setProperty('volume', request.volume)
        self.__engine.setProperty('rate', request.rate)
        self.__engine.setProperty('voice', request.language)

        self.__engine.say(request.text)

        self.__engine.runAndWait()

        goal_handle.succeed()

        return result


def main(args=None):
    rclpy.init(args=args)

    node = TtsNode()

    node.join_spin()

    node.destroy()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
