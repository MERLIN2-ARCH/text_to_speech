from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable


def generate_launch_description():
    pkg_name = "text_to_speech"
    namespace = "text_to_speech"

    stdout_linebuf_envvar = SetEnvironmentVariable(
        "RCUTILS_CONSOLE_STDOUT_LINE_BUFFERED", "1"
    )

    #
    # NODES
    #
    tts_node_cmd = Node(
        package=pkg_name,
        executable="tts_node",
        name="tts_node",
        namespace=namespace,
    )

    ld = LaunchDescription()

    ld.add_action(stdout_linebuf_envvar)

    ld.add_action(tts_node_cmd)

    return ld
