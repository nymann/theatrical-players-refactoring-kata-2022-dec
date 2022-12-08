from abc import ABC
from abc import abstractmethod
import math
from typing import Any, Type


def format_as_dollars(amount):
    return f"${amount:0,.2f}"


def statement(invoice: dict[str, Any], plays: dict[str, dict[str, str]]) -> str:
    total_amount: float = 0
    volume_credits: float = 0
    result = f'Statement for {invoice["customer"]}\n'

    for perf in invoice["performances"]:
        play_dict = plays[perf["playID"]]
        play: Play = PlayFactory.create_play(play_dict=play_dict, perf=perf)
        volume_credits += play.volume_credits()
        result += f' {play_dict["name"]}: {format_as_dollars(play.price()/100)} ({perf["audience"]} seats)\n'
        total_amount += play.price()

    result += f"Amount owed is {format_as_dollars(total_amount/100)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result


class Play(ABC):
    def __init__(self, perf: dict) -> None:
        self.perf = perf
        self.audience: int = perf["audience"]

    def volume_credits(self) -> float:
        return max(self.audience - 30, 0)

    @abstractmethod
    def price(self) -> float:
        raise NotImplementedError


class TragedyPlay(Play):
    def price(self) -> float:
        result = 40000
        if self.audience > 30:
            result += 1000 * (self.audience - 30)
        return result


class ComedyPlay(Play):
    def price(self) -> float:
        this_amount = 30000
        if self.audience > 20:
            this_amount += 10000 + 500 * (self.audience - 20)

        this_amount += 300 * self.audience
        return this_amount

    def volume_credits(self) -> float:
        volume_credits = super().volume_credits()
        volume_credits += math.floor(self.audience / 5)
        return volume_credits


class PlayFactory:
    _plays = {"comedy": ComedyPlay, "tragedy": TragedyPlay}

    @classmethod
    def create_play(cls, play_dict: dict, perf: dict) -> Play:
        play_type = play_dict["type"]
        try:
            play_klass: Type[Play] = cls._plays[play_type]
        except KeyError:
            raise ValueError(f"unknown type: {play_type}")
        return play_klass(perf=perf)
