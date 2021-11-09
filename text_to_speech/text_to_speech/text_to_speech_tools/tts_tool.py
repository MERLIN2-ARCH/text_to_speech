
from text_to_speech_interfaces.action import TTS
from subprocess import Popen
from abc import ABC, abstractmethod


class TtsTool(ABC):
    """
    The TtsTool interface declares operations common to all supported versions
    of tts.
    """

    @abstractmethod
    def say(self, request: TTS.Goal) -> Popen:
        pass
