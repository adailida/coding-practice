# Day 3 (2026-10-16): 3 repeats + 2 new. Write your own imports and signatures.


# 1. Return the character that appears most often in a string. Use Counter.
#    (Repeat: most_common, new wording)
from collections import Counter, defaultdict, deque


def most_common_char(s: str) -> str | None:
    result = Counter(s).most_common(n=1)
    return result[0][0] if result else None


assert most_common_char("banana") == "a"
assert most_common_char("mississippi!") in ("i", "s")


# 2. Group names by their first letter. Use defaultdict(list).
#    (Repeat: grouping)
def by_first_letter(words: list[str]) -> dict[str, list[str]]:
    d = defaultdict(list)
    for word in words:
        if not word:
            continue
        d[word[0]].append(word)
    return d


assert by_first_letter(["ann", "bob", "amy", "ben", "cy"]) == {
    "a": ["ann", "amy"],
    "b": ["bob", "ben"],
    "c": ["cy"],
}


# 3. Return the last n lines of a text, joined back with newlines.
#    Use deque with maxlen. Must work when n is 0 or bigger than the line count.
#    (Repeat: deque maxlen, now on lines)
def tail(text: str, n: int) -> str:
    d = deque(text.splitlines(), maxlen=n)
    return "\n".join(d)


assert tail("one\ntwo\nthree\nfour", 2) == "three\nfour"
assert tail("one\ntwo", 5) == "one\ntwo"
assert tail("one\ntwo", 0) == ""


# 4. Sort (name, age) tuples: oldest first, ties broken by name A to Z.
#    One call to sorted with a key. No reverse=True.
#    (New: sort keys)
def by_age_then_name(lst: list[tuple[str, int]]) -> list[tuple[str, int]]:
    return sorted(lst, key=lambda x: (-x[1], x[0]))


assert by_age_then_name([("cat", 30), ("ann", 25), ("bob", 30), ("dan", 25)]) == [
    ("bob", 30),
    ("cat", 30),
    ("ann", 25),
    ("dan", 25),
]


# 5. Swap a dict's keys and values in one line. Use a dict comprehension.
#    (New: comprehensions)
def invert(d: dict[str, int]) -> dict[int, str]:
    return {v: k for k, v in d.items()}


assert invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}
assert invert({}) == {}
