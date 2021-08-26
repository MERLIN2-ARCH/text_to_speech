
import subprocess
from .tts_tool import TtsTool


class SpdSayTtsTool(TtsTool):

    def say(self, request):
        gender_dict = {"m": "male", "f": "female"}
        return subprocess.Popen(
            args=["spd-say",
                  "-l" + request.config.language,
                  "-t", gender_dict[request.config.gender] + "1",
                  "-r", str(request.config.rate - 100),
                  "-i", str(request.config.volume * 200 - 100),
                  request.text,
                  "--wait"
                  ],
            stdout=subprocess.PIPE,
            start_new_session=True)
