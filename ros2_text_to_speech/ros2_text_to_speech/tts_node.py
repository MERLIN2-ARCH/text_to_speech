
""" Text to Speech for ROS2 """

import rclpy
from action_msgs.msg import GoalStatus
from ros2_text_to_speech_interfaces.action import TTS
from ros2_text_to_speech_interfaces.msg import Config
from .ros2_text_to_speech_tools import (
    EspeakTtsTool,
    SayTtsTool,
    SpdSayTtsTool,
    FestivalTtsTool
)
from custom_ros2 import (
    Node,
    ActionSingleServer
)


class TtsNode(Node):
    """ TTS Node Class """

    def __init__(self):

        super().__init__('tts_node')

        self.__process = None

        self.__tools_dict = {
            Config.ESPEAK: EspeakTtsTool(),
            Config.SAY: SayTtsTool(),
            Config.SPD_SAY: SpdSayTtsTool(),
            Config.FESTIVAL: FestivalTtsTool()
        }

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
        if self.__process:
            self.__process.terminate()

    def __execute_server(self, goal_handle):
        """ execute action server

        Args:
            goal_handle: goal_handle
        """

        request = goal_handle.request
        result = TTS.Result()

        if request.config.tool not in self.__tools_dict:
            goal_handle.abort()
            return result

        self.__process = self.__tools_dict[request.config.tool].say(request)
        self.__process.wait()

        if(goal_handle.status != GoalStatus.STATUS_CANCELED and
                goal_handle.status != GoalStatus.STATUS_CANCELING):
            goal_handle.succeed()
        else:
            goal_handle.canceled()

        return result


def main(args=None):
    rclpy.init(args=args)

    node = TtsNode()

    node.join_spin()

    node.destroy()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
