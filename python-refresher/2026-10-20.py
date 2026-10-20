# Day 5 (2026-10-20): 3 repeats + 2 new. Write your own imports and signatures.


# 1. Return the total cost of a cart given as (price, quantity) pairs.
#    One line: sum() over the pairs, unpacking each one. No index access, no list brackets.
#    (Repeat: unpacking, generator into sum)
import itertools


def cart_total(cart: list[tuple[float, int]]) -> float:
    return sum(price * quantity for price, quantity in cart)


assert (got := cart_total([(2.5, 2), (1.25, 4)])) == 10.0, f"{got=}"
assert (got := cart_total([])) == 0, f"{got=}"


# 2. Count the lines of a text that have more than n words. Blank lines have 0 words.
#    One line, using splitlines. (Repeat: splitlines, ">" boundary, generator into sum)
def long_lines(s: str, n: int) -> int:
    return sum(1 for line in s.splitlines() if len(line.split()) > n)


assert (got := long_lines("a b c\nd e\n\nf g h i\n", 2)) == 2, f"{got=}"
assert (got := long_lines("a b\nc d", 2)) == 0, f"{got=}"
assert (got := long_lines("", 0)) == 0, f"{got=}"


# 3. Format a label: name right-aligned in 5 characters, a space, then a share
#    (a float from 0 to 1) shown as a percent with 1 decimal. One f-string.
#    (Repeat: width and alignment; new: the percent spec)
def share_label(s: str, f: float) -> str:
    return f"{s:>5} {f:.1%}"


assert (got := share_label("al", 0.125)) == "   al 12.5%", f"{got=}"
assert (got := share_label("bobby", 1.0)) == "bobby 100.0%", f"{got=}"


# 4. Return the running totals of a list of numbers.
#    Use itertools.accumulate, no loop. (New: itertools)
def running_totals(totals: list[int]) -> list[int]:
    return list(itertools.accumulate(totals))


assert (got := running_totals([3, 1, 4, 1])) == [3, 4, 8, 9], f"{got=}"
assert (got := running_totals([])) == [], f"{got=}"


# 5. Turn a number of seconds into "M:SS". Use divmod and a zero-padding spec.
#    (New: divmod, padding)
def mm_ss(s: int) -> str:
    m, s = divmod(s, 60)
    return f"{m}:{s:02d}"


assert (got := mm_ss(125)) == "2:05", f"{got=}"
assert (got := mm_ss(59)) == "0:59", f"{got=}"
assert (got := mm_ss(600)) == "10:00", f"{got=}"
