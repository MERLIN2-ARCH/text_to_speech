
""" Text to Speech for ROS2 """

import os
import time
import signal
import rclpy
from ros2_text_to_speech_interfaces.action import TTS
from ros2_text_to_speech_interfaces.msg import Config

from simple_node import Node

from .ros2_text_to_speech_tools import (
    EspeakTtsTool,
    SpdSayTtsTool,
    FestivalTtsTool,
    GTtsTtsTool
)


class TtsNode(Node):
    """ TTS Node Class """

    def __init__(self):

        super().__init__('tts_node')

        self.__process = None

        self.__tools_dict = {
            Config.ESPEAK: EspeakTtsTool(),
            Config.SPD_SAY: SpdSayTtsTool(),
            Config.FESTIVAL: FestivalTtsTool(),
            Config.GTTS: GTtsTtsTool()
        }

        # action server
        self.__action_server = self.create_action_server(TTS,
                                                         "tts",
                                                         execute_callback=self.__execute_server,
                                                         cancel_callback=self.__cancel_callback
                                                         )

    def __cancel_callback(self):
        if self.__process:
            while self.__process == "started":
                time.sleep(0.05)

            os.killpg(os.getpgid(self.__process.pid), signal.SIGTERM)

    def __execute_server(self, goal_handle):
        """ execute action server

        Args:
            goal_handle: goal_handle
        """

        self.__process = "started"

        request = goal_handle.request
        result = TTS.Result()

        if request.config.tool not in self.__tools_dict:
            goal_handle.abort()
            return result

        self.__process = self.__tools_dict[request.config.tool].say(request)
        self.__process.wait()

        if self.__action_server.is_canceled():
            self.__action_server.wait_for_canceling()
            goal_handle.canceled()

        else:
            goal_handle.succeed()

        return result


def main(args=None):
    rclpy.init(args=args)

    node = TtsNode()

    node.join_spin()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
