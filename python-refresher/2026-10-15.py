# Day 2 (2026-10-15): collections, repeat from blank. Write your own imports.
from collections import Counter, defaultdict, deque
from collections.abc import Iterable
from typing import Any


# 1. Return the k most common words with their counts, most common first.
#    Use Counter.
def top_k(words: list[str], k: int) -> list[tuple[str, int]]:
    return Counter(words).most_common(k)


assert top_k("a b a c a b".split(), 2) == [("a", 3), ("b", 2)]  # pyright: ignore[reportArgumentType]


# 2. Group words by their length. Use defaultdict(list).
def group_by_len(lst: list[str]) -> dict[int, list[str]]:
    d = defaultdict(list)
    for s in lst:
        d[len(s)].append(s)
    return d


assert group_by_len(["hi", "yo", "hey"]) == {2: ["hi", "yo"], 3: ["hey"]}


# 3. Group words that are anagrams of each other. Return a list of groups.
def group_anagrams(lst: list[str]) -> list[list[str]]:
    d = defaultdict(list)
    for w in lst:
        d["".join(sorted(w))].append(w)
    return list(d.values())


assert sorted(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == [
    ["bat"],
    ["eat", "tea", "ate"],
    ["tan", "nat"],
]


# 4. Return the last n items of any iterable as a list, in one line.
#    Use deque with maxlen.
def last_n(lst: Iterable[Any], n: int) -> list[Any]:
    return list(deque(lst, maxlen=n))


assert last_n(range(10), 3) == [7, 8, 9]


# 5a. Rotate a list right by k. Use deque.rotate.
def rotate(lst: list[Any], k: int) -> list[Any]:
    d = deque(lst)
    d.rotate(k)
    return list(d)


assert rotate([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


# 5b. Check for a palindrome by popping from both ends of a deque
#     (popleft and pop). No slicing.
def is_pal(w: str) -> bool:
    d = deque(w)
    while len(d) > 1:
        if d.pop() != d.popleft():
            return False
    return True


assert is_pal("racecar") and is_pal("") and not is_pal("ab")
