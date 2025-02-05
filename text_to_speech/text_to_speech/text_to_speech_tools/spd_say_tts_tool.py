from text_to_speech_msgs.action import TTS
from subprocess import Popen, PIPE
from text_to_speech.text_to_speech_tools.tts_tool import TtsTool


class SpdSayTtsTool(TtsTool):

    def say(self, request: TTS.Goal) -> Popen:
        gender_dict = {"m": "male", "f": "female"}
        return Popen(
            args=[
                "spd-say",
                "-l" + request.config.language,
                "-t",
                gender_dict[request.config.gender] + "1",
                "-r",
                str(request.config.rate - 100),
                "-i",
                str(request.config.volume * 200 - 100),
                request.text,
                "--wait",
            ],
            stdout=PIPE,
            start_new_session=True,
        )
