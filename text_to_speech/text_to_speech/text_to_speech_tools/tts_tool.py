

from abc import ABC, abstractmethod


class TtsTool(ABC):
    """
    The TtsTool interface declares operations common to all supported versions
    of tts.
    """

    @abstractmethod
    def say(self, request):
        pass
