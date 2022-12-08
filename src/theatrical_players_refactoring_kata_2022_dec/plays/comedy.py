import math

from theatrical_players_refactoring_kata_2022_dec.plays.play import Play


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
