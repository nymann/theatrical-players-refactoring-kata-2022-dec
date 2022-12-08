from __future__ import annotations

from typing import Any

from theatrical_players_refactoring_kata_2022_dec.play_factory import PlayFactory
from theatrical_players_refactoring_kata_2022_dec.plays.play import Play
from theatrical_players_refactoring_kata_2022_dec.renderers.statement import StatementRenderer


class Statement:
    def __init__(self, plays: list[Play], customer: str) -> None:
        self.plays = plays
        self.customer = customer

    def generate(self, renderer: StatementRenderer) -> str:
        return renderer.render(plays=self.plays, customer=self.customer)

    @classmethod
    def from_dicts(cls, invoice: dict[str, Any], plays: dict[str, dict[str, str]]) -> Statement:
        result: list[Play] = []
        for perf in invoice["performances"]:
            play_dict = plays[perf["playID"]]
            result.append(PlayFactory.create_play(play_dict=play_dict, perf=perf))
        customer = invoice["customer"]
        return cls(plays=result, customer=customer)
