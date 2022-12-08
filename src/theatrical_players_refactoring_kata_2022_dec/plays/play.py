from abc import ABC
from abc import abstractmethod


class Play(ABC):
    def __init__(self, perf: dict, play_dict: dict) -> None:
        self.perf = perf
        self.audience: int = perf["audience"]
        self.name = play_dict["name"]

    def volume_credits(self) -> float:
        return max(self.audience - 30, 0)

    @abstractmethod
    def price(self) -> float:
        raise NotImplementedError
