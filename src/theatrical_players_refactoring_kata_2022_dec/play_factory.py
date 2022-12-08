from typing import Type

from theatrical_players_refactoring_kata_2022_dec.plays.comedy import ComedyPlay
from theatrical_players_refactoring_kata_2022_dec.plays.play import Play
from theatrical_players_refactoring_kata_2022_dec.plays.tragedy import TragedyPlay


class PlayFactory:
    _play_types = {"comedy": ComedyPlay, "tragedy": TragedyPlay}

    @classmethod
    def create_play(cls, play_dict: dict, perf: dict) -> Play:
        play_type = play_dict["type"]
        try:
            play_klass: Type[Play] = cls._play_types[play_type]
        except KeyError:
            raise ValueError(f"unknown type: {play_type}")
        return play_klass(perf=perf, play_dict=play_dict)
