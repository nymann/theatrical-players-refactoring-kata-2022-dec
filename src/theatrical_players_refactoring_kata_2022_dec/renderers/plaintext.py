from theatrical_players_refactoring_kata_2022_dec.plays.play import Play
from theatrical_players_refactoring_kata_2022_dec.statement import StatementRenderer


class PlaintextStatementRenderer(StatementRenderer):
    def render(self, plays: list[Play], customer: str) -> str:
        result = f"Statement for {customer}\n"
        total_amount: float = 0
        volume_credits: float = 0
        for play in plays:
            result += f" {play.name}: {self.format_as_dollars(play.price()/100)} ({play.audience} seats)\n"
            total_amount += play.price()
            volume_credits += play.volume_credits()

        result += f"Amount owed is {self.format_as_dollars(total_amount/100)}\n"
        result += f"You earned {volume_credits} credits\n"
        return result
