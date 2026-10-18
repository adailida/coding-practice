# Day 4 (2026-10-18): 3 repeats + 2 new. Write your own imports and signatures.


# 1. Return the first non-empty string in a list, or None if there isn't one.
#    No len(). (Repeat: truthiness)
import heapq
from collections import Counter


def first_non_empty(lst: list[str]) -> str | None:
    for s in lst:
        if s:
            return s
    return None


assert first_non_empty(["", "", "hi", "yo"]) == "hi"
assert first_non_empty(["", ""]) is None
assert first_non_empty([]) is None


# 2. Return the names whose score is above a limit, sorted A to Z.
#    One line, using the dict's key-value pairs. (Repeat: .items() unpacking)
def above(d: dict[str, int], limit: int) -> list[str]:
    return sorted(name for name, score in d.items() if score > limit)


assert above({"bo": 7, "al": 9, "cy": 3}, 5) == ["al", "bo"]
assert above({}, 5) == []


# 3. Count how many words start with each letter, ignoring case.
#    The text may have several lines and blank lines. Use Counter.
#    (Repeat: Counter, splitting text)
def count_first_letters(s: str) -> Counter[str]:
    return Counter(item[0].lower() for item in s.split())


assert count_first_letters("Apple ant\nbee Bat\n\ncat") == {"a": 2, "b": 2, "c": 1}
assert count_first_letters("") == {}


# 4. Return the names of the two highest scorers, highest first.
#    Use heapq.nlargest with a key. No sorting. (New: heapq)
def top_two(lst: list[tuple[str, float]]) -> list[str]:
    return [name for name, _ in heapq.nlargest(2, lst, key=lambda x: x[1])]


assert top_two([("al", 7.5), ("bo", 9.0), ("cy", 8.25)]) == ["bo", "cy"]
assert top_two([("al", 1.0)]) == ["al"]


# 5. Format one table row: name left-aligned in 6 characters, a "|",
#    then the score right-aligned in 7 characters with 2 decimals.
#    One f-string. (New: format specs)
def row(s: str, n: float) -> str:
    return f"{s:<6.6}|{n:7.2f}"


assert row("al", 7.5) == "al    |   7.50"
assert row("bob", 123.456) == "bob   | 123.46"
