from text_to_speech_msgs.action import TTS
from subprocess import Popen, PIPE
from text_to_speech.text_to_speech_tools.tts_tool import TtsTool


class FestivalTtsTool(TtsTool):

    def say(self, request: TTS.Goal) -> Popen:
        language_dict = {"es": "spanish", "en": "english"}

        language = "english"

        if request.config.language in language_dict:
            language = language_dict[request.config.language]

        return Popen(
            "echo " + request.text + " | festival --tts --language " + language,
            shell=True,
            stdout=PIPE,
            start_new_session=True,
        )
