from abc import ABC
from abc import abstractmethod

from theatrical_players_refactoring_kata_2022_dec.plays.play import Play


class StatementRenderer(ABC):
    @abstractmethod
    def render(self, plays: list[Play], customer: str) -> str:
        raise NotImplementedError

    def format_as_dollars(self, amount):
        return f"${amount:0,.2f}"
