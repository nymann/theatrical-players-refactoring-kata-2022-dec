import json

from approval_utilities.utils import get_adjacent_file
from approvaltests import verify

from theatrical_players_refactoring_kata_2022_dec.renderers.plaintext import PlaintextStatementRenderer
from theatrical_players_refactoring_kata_2022_dec.statement import Statement


def test_example_statement():
    renderer = PlaintextStatementRenderer()
    with open(get_adjacent_file("invoice.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("plays.json")) as f:
        plays = json.loads(f.read())

    statement = Statement.from_dicts(invoice=invoice, plays=plays)
    verify(renderer.render(statement))


def test_statement_with_new_play_types():
    renderer = PlaintextStatementRenderer()
    with open(get_adjacent_file("invoice_new_plays.json")) as f:
        invoice = json.loads(f.read())
    with open(get_adjacent_file("new_plays.json")) as f:
        plays = json.loads(f.read())
    statement = Statement.from_dicts(invoice=invoice, plays=plays)
    verify(renderer.render(statement))
