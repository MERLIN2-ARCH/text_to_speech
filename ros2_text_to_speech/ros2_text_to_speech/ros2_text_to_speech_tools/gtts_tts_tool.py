
import subprocess
from .tts_tool import TtsTool
from gtts import gTTS


class GTtsTtsTool(TtsTool):

    def say(self, request):

        slow = False
        gtts_file = "/tmp/gtts_tmp_file.mp3"

        if request.config.rate < 100:
            slow = True

        gtts_obj = gTTS(text=request.text,
                        lang=request.config.language, slow=slow)

        gtts_obj.save(gtts_file)

        return subprocess.Popen(
            args=["mpg321",
                  gtts_file
                  ],
            stdout=subprocess.PIPE,
            start_new_session=True)
