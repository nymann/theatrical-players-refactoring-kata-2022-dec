from theatrical_players_refactoring_kata_2022_dec.plays.play import Play


class TragedyPlay(Play):
    def price(self) -> float:
        result = 40000
        if self.audience > 30:
            result += 1000 * (self.audience - 30)
        return result
