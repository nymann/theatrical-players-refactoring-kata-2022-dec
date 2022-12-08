from abc import ABC
from abc import abstractmethod

from theatrical_players_refactoring_kata_2022_dec.statement import Statement


class StatementRenderer(ABC):
    @abstractmethod
    def render(self, statement: Statement) -> str:
        raise NotImplementedError

    def format_as_dollars(self, amount):
        return f"${amount:0,.2f}"
