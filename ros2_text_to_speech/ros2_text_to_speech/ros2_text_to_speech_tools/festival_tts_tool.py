
import subprocess
from .tts_tool import TtsTool


class FestivalTtsTool(TtsTool):

    def say(self, request):
        language_dict = {"es": "spanish", "en": "english"}

        language = "english"

        if request.config.language in language_dict:
            language = language_dict[request.config.language]

        return subprocess.Popen(
            "echo " + request.text + " | festival --tts --language " + language,
            shell=True,
            stdout=subprocess.PIPE)
