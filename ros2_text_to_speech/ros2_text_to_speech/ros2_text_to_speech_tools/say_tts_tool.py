
import subprocess
from .tts_tool import TtsTool


class SayTtsTool(TtsTool):

    def say(self, request):
        return subprocess.Popen(
            args=["say",
                  request.text
                  ],
            stdout=subprocess.PIPE)
