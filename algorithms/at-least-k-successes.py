# A funder backs a portfolio of independent projects. Project i succeeds with
# probability ps[i] (a float from 0 to 1), whatever happens to the others.

# Part 1. Write expected_successes(ps): the expected number of projects that succeed.

# expected_successes([0.9, 0.2, 0.5])     # about 1.6
# expected_successes([])                  # 0

# Part 2. Write prob_at_least(ps, k): the probability that at least k projects succeed.

# There can be up to 1,000 projects, so listing every success/failure combination
# (2 to the power of n of them) is too slow.

# prob_at_least([0.5, 0.5], 1)            # 0.75
# prob_at_least([0.5, 0.5], 2)            # 0.25
# prob_at_least([0.9, 0.2, 0.5], 2)       # about 0.55
# prob_at_least([0.3], 0)                 # 1.0   (zero successes always happens)
# prob_at_least([0.3], 2)                 # 0.0   (more than there are projects)
import math


def expected_successes(ps: list[float]) -> float:
    return sum(ps)


assert math.isclose(expected_successes([0.9, 0.2, 0.5]), 1.6)
assert math.isclose(expected_successes([]), 0)


def prob_at_least(ps: list[float], k: int) -> float:
    if k <= 0:
        return 1.0

    dp = [0.0] * (len(ps) + 1)
    dp[0] = 1.0

    for p in ps:
        q = 1 - p
        for j in range(len(ps), 0, -1):
            dp[j] = dp[j] * q + dp[j - 1] * p
        dp[0] = dp[0] * q

    return sum(dp[k:], 0.0)


assert math.isclose(prob_at_least([0.5, 0.5], -1), 1.0)
assert math.isclose(prob_at_least([0.5, 0.5], 1), 0.75)
assert math.isclose(prob_at_least([0.5, 0.5], 2), 0.25)
assert math.isclose(prob_at_least([0.9, 0.2, 0.5], 2), 0.55)
assert math.isclose(prob_at_least([0.3], 0), 1.0)
assert math.isclose(prob_at_least([0.3], 2), 0.0, abs_tol=0.000001)
