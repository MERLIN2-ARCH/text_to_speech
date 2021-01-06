
import subprocess
from .tts_tool import TtsTool


class EspeakTtsTool(TtsTool):

    def say(self, request):
        return subprocess.Popen(
            args=["espeak",
                  "-v" + request.config.language + "+" + request.config.gender + "1",
                  "-s", str(request.config.rate + 75),
                  "-a", str(request.config.volume * 200),
                  request.text
                  ],
            stdout=subprocess.PIPE,
            start_new_session=True)
