import math
from typing import Any


def format_as_dollars(amount):
    return f"${amount:0,.2f}"


def statement(invoice: dict[str, Any], plays: dict[str, dict[str, str]]) -> str:
    total_amount: float = 0
    volume_credits: float = 0
    result = f'Statement for {invoice["customer"]}\n'

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        if play["type"] == "tragedy":
            this_amount = tragedy_play_price(perf=perf)
        elif play["type"] == "comedy":
            this_amount = comedy_play_price(perf=perf)
        else:
            raise ValueError(f'unknown type: {play["type"]}')

        # add volume credits
        volume_credits += max(perf["audience"] - 30, 0)
        # add extra credit for every ten comedy attendees
        if "comedy" == play["type"]:
            volume_credits += math.floor(perf["audience"] / 5)
        # print line for this order
        result += f' {play["name"]}: {format_as_dollars(this_amount/100)} ({perf["audience"]} seats)\n'
        total_amount += this_amount

    result += f"Amount owed is {format_as_dollars(total_amount/100)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result


def tragedy_play_price(perf: dict) -> float:
    result = 40000
    if perf["audience"] > 30:
        result += 1000 * (perf["audience"] - 30)
    return result


def comedy_play_price(perf: dict) -> float:
    this_amount = 30000
    if perf["audience"] > 20:
        this_amount += 10000 + 500 * (perf["audience"] - 20)

    this_amount += 300 * perf["audience"]
    return this_amount
