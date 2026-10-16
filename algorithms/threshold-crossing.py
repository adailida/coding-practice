# In the S-Process, each recommender gives every application a marginal value function: how much the
# next dollar is worth, given how many dollars it already has. More money means each extra dollar is
# worth the same or less, so the function is non-increasing.

# Write last_worth_funding(mv, t, cap):

# - mv: a function from an integer dollar amount x (0 or more) to a float, the value of the dollar
#   after x. It is non-increasing. Treat it as a black box: you can call it, but you can't see
#   inside it.
# - t: a threshold. A dollar is worth funding only if its marginal value is at least t.
# - cap: the largest amount you may consider. It can be as big as 1,000,000,000.

# Return the largest x in [0, cap] where mv(x) >= t. If even mv(0) is below t, return None.

# Constraint: each call to mv is expensive (pretend it runs a simulation), so walking up from 0 one
# dollar at a time is too slow.

# Examples, using mv = lambda x: 1000 / (1 + x):

# last_worth_funding(mv, 10, 1_000_000)      # 99    (mv(99) = 10.0, mv(100) is about 9.9)
# last_worth_funding(mv, 2000, 1_000_000)    # None  (mv(0) = 1000 is already below 2000)
# last_worth_funding(mv, 0.5, 1000)          # 1000  (still worth it at the cap)
# last_worth_funding(mv, 1000, 10**9)        # 0     (only x = 0 qualifies)

from collections.abc import Callable


def last_worth_funding(mv: Callable[[int], float], t: float, cap: int) -> int | None:
    return _last_worth_funding(mv, t, (0, cap))


def _last_worth_funding(mv: Callable[[int], float], t: float, cap: tuple[int, int]) -> int | None:
    cap_from, cap_to = cap
    if cap_to - cap_from < 0:
        return None

    x = cap_from + (cap_to - cap_from) // 2
    val: float = mv(x)
    # print(f"{x=} {val=}")

    if val < t:
        return _last_worth_funding(mv, t, (cap_from, x - 1))
    else:
        return _last_worth_funding(mv, t, (x + 1, cap_to)) or x


def mv(x: int) -> float:
    return 1000 / (1 + x)


assert last_worth_funding(mv=mv, t=10, cap=1_000_000) == 99
assert last_worth_funding(mv=mv, t=2000, cap=1_000_000) is None
assert last_worth_funding(mv=mv, t=0.5, cap=1000) == 1000
assert last_worth_funding(mv=mv, t=1000, cap=10**9) == 0
assert last_worth_funding(mv=mv, t=1000, cap=0) == 0
assert last_worth_funding(lambda x: 1000, t=1000, cap=10000) == 10000
