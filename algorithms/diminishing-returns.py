# Problem

# A funder estimates how much good a charity does per dollar.
# The first dollars do the most good, and each later dollar does less. This is given as tiers,
# in order:

# tiers = [(100, 3), (200, 2), (300, 1)]

# Each tuple is (width, rate):
# - the first 100 dollars produce 3 units of value per dollar
# - the next 200 dollars produce 2 per dollar
# - the next 300 dollars produce 1 per dollar
# - any dollar beyond the last tier produces 0

# Write value(amount, tiers) that returns the total value of giving amount dollars.

# Example: value(150, tiers) returns 400. The first 100 dollars give 100 × 3 = 300,
# and the next 50 give 50 × 2 = 100.


import pytest


def value(amount: float, tiers: list[tuple[int, int]]) -> float:
    result = 0
    remaining = amount
    for tier_width, tier_rate in tiers:
        if remaining <= 0:
            break
        result += min(tier_width, remaining) * tier_rate
        remaining -= tier_width
    return result


assert (value(amount=150, tiers=[(100, 3), (200, 2), (300, 1)])) == 400
assert (value(amount=100, tiers=[(100, 3), (200, 2), (300, 1)])) == 300
assert (value(amount=2.5, tiers=[(100, 3), (200, 2), (300, 1)])) == 7.5
assert (value(amount=99, tiers=[(100, 3), (200, 2), (300, 1)])) == 297
assert (value(amount=700, tiers=[(100, 3), (200, 2), (300, 1)])) == 1000
assert (value(amount=0, tiers=[(100, 3), (200, 2), (300, 1)])) == 0


# The funder now asks the opposite question: "I want to reach a target amount of value.
# What is the smallest amount of money that gets me there?"

# Write amount_for(target, tiers) in the same file. Use the same tiers as before.


# Examples:
# - amount_for(400, tiers) returns 150
# - amount_for(301, tiers) returns 100.5
def amount_for(target_value: float, tiers: list[tuple[int, int]]) -> float | None:
    result = 0
    remaining_value = target_value
    for tier_width, tier_rate in tiers:
        if remaining_value <= 0:
            break
        tier_value = min(tier_width * tier_rate, remaining_value)
        result += tier_value / tier_rate
        remaining_value -= tier_value
    return result if remaining_value == 0 else None


assert amount_for(400, [(100, 3), (200, 2), (300, 1)]) == pytest.approx(150)
assert amount_for(301, [(100, 3), (200, 2), (300, 1)]) == pytest.approx(100.5)
assert amount_for(1000, [(100, 3), (200, 2), (300, 1)]) == pytest.approx(600)
assert amount_for(1001, [(100, 3), (200, 2), (300, 1)]) is None
