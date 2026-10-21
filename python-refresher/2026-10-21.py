# Day 6 (2026-10-21): 3 repeats + 2 new. Write your own imports and signatures.


# 1. Return the n most common words in a text, most common first, ignoring case.
#    The text may have double spaces, tabs and blank lines. Use Counter.
#    Name it top_words(text, n). (Repeat: Counter, split with no argument)
import bisect
from collections import Counter
from dataclasses import dataclass


def top_words(s: str, n: int) -> list[str]:
    c = Counter(s.lower().split())
    return [w for w, _ in c.most_common(n)]


assert (got := top_words("The cat\n\nthe  dog\tTHE end dog", 2)) == ["the", "dog"], f"{got=}"
assert (got := top_words("a  b b\n\n\tc c c", 1)) == ["c"], f"{got=}"
assert (got := top_words("", 3)) == [], f"{got=}"


# 2. Count how many (name, score) pairs scored at least the pass mark.
#    One line: unpack each pair, no index access, no len().
#    Name it passed(results, mark). (Repeat: boundary wording, generator into sum)
def passed(results: list[tuple[str, int]], mark: int) -> int:
    return sum(1 for _, score in results if score >= mark)


assert (got := passed([("al", 70), ("bo", 69), ("cy", 85)], 70)) == 2, f"{got=}"
assert (got := passed([("al", 50)], 70)) == 0, f"{got=}"
assert (got := passed([], 70)) == 0, f"{got=}"


# 3. Sort words longest first, ties broken A to Z.
#    One call to sorted with a key. No reverse=True.
#    Name it by_length(words). (Repeat: sort keys, now on strings)
def by_length(words: list[str]) -> list[str]:
    return sorted(words, key=lambda s: (-len(s), s))


words = ["fig", "kiwi", "apple", "date", "pear"]
assert (got := by_length(words)) == ["apple", "date", "kiwi", "pear", "fig"], f"{got=}"
assert (got := by_length([])) == [], f"{got=}"


# 4. Turn a score (0 to 100) into a letter grade:
#    below 60 is F, 60 to 69 is D, 70 to 79 is C, 80 to 89 is B, 90 and up is A.
#    Use bisect on a list of cutoffs. No if/elif chain.
#    Name it grade(score). (New: bisect)
def grade(score: int) -> str:
    breakpoints = [60, 70, 80, 90]
    grades = ["F", "D", "C", "B", "A"]
    return grades[bisect.bisect(breakpoints, score)]


assert (got := grade(59)) == "F", f"{got=}"
assert (got := grade(60)) == "D", f"{got=}"
assert (got := grade(70)) == "C", f"{got=}"
assert (got := grade(89)) == "B", f"{got=}"
assert (got := grade(90)) == "A", f"{got=}"
assert (got := grade(100)) == "A", f"{got=}"
assert (got := grade(0)) == "F", f"{got=}"


# 5. Make a dataclass Item with fields name (str), price (float) and qty (int, default 1).
#    Then return the name of the cheapest item by price. Use min with a key.
#    Name it cheapest(items). (New: dataclass)
@dataclass
class Item:
    name: str
    price: float
    qty: int = 1


def cheapest(items: list[Item]) -> str | None:
    return (
        result.name
        if (result := min(items, default=None, key=lambda i: i.price)) is not None
        else None
    )


assert (got := Item("pen", 1.5).qty) == 1, f"{got=}"
assert (got := repr(Item("pen", 1.5))) == "Item(name='pen', price=1.5, qty=1)", f"{got=}"
assert Item("pen", 1.5, 2) == Item("pen", 1.5, 2), "dataclasses compare by field values"
items = [Item("ink", 4.0, 3), Item("pen", 1.5), Item("pad", 2.25)]
assert (got := cheapest(items)) == "pen", f"{got=}"
assert (got := cheapest([])) is None, f"{got=}"
