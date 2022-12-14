from theatrical_players_refactoring_kata_2022_dec.plays.play import Play
from theatrical_players_refactoring_kata_2022_dec.renderers.statement import StatementRenderer
from theatrical_players_refactoring_kata_2022_dec.statement import Statement


class PlaintextStatementRenderer(StatementRenderer):
    def render(self, statement: Statement) -> str:
        result: list[str] = [f"Statement for {statement.customer}"]
        for play in statement.plays:
            result.append(self._format_play(play=play))

        result.append(self._amount_owned(statement=statement))
        result.append(f"You earned {statement.volume_credits} credits")
        return "\n".join(result)

    def _format_play(self, play: Play) -> str:
        dollar_price = self.format_as_dollars(play.price() / 100)
        return f" {play.name}: {dollar_price} ({play.audience} seats)"

    def _amount_owned(self, statement: Statement) -> str:
        amount_owned = self.format_as_dollars(statement.total_amount / 100)
        return f"Amount owed is {amount_owned}"
