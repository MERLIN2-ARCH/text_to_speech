
from text_to_speech_interfaces.action import TTS
from subprocess import Popen, PIPE
from .tts_tool import TtsTool


class ESpeakTtsTool(TtsTool):

    def say(self, request: TTS.Goal) -> Popen:
        return Popen(
            args=["espeak",
                  "-v" + request.config.language + "+" + request.config.gender + "1",
                  "-s", str(request.config.rate + 75),
                  "-a", str(request.config.volume * 200),
                  request.text
                  ],
            stdout=PIPE,
            start_new_session=True)
