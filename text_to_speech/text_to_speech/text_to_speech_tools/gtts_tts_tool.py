
from text_to_speech_interfaces.action import TTS
from subprocess import Popen, PIPE
from .tts_tool import TtsTool
from gtts import gTTS


class GTtsTtsTool(TtsTool):

    def say(self, request: TTS.Goal) -> Popen:

        slow = False
        gtts_file = "/tmp/gtts_tmp_file.mp3"

        if request.config.rate < 100:
            slow = True

        gtts_obj = gTTS(text=request.text,
                        lang=request.config.language, slow=slow)

        gtts_obj.save(gtts_file)

        return Popen(
            args=["mpg321",
                  "--stereo",
                  "-g", str(request.config.volume * 100),
                  gtts_file
                  ],
            stdout=PIPE,
            start_new_session=True)
