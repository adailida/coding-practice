# Day 7 (2026-10-22): 3 repeats + 2 new. Write your own imports and signatures.
# Theme: the Python behind today's exercise (stateful implementation).


# 1. Group (key, value) events by key, values in arrival order.
#    Use defaultdict, unpack each pair, no index access.
#    Name it history(events). (Repeat: defaultdict, unpacking, type hint on an empty start)
from collections import OrderedDict, defaultdict
from dataclasses import dataclass, field
from typing import Any


def history(events: list[tuple[str, int]]) -> dict[str, list[int]]:
    d: defaultdict[Any, list[int]] = defaultdict(list)
    for k, v in events:
        d[k].append(v)
    return d


assert (got := history([("a", 1), ("b", 2), ("a", 3)])) == {"a": [1, 3], "b": [2]}, f"{got=}"
assert (got := history([])) == {}, f"{got=}"


# 2. Return the item with the lowest count, or None when the stock is empty.
#    One call to min. No if, no loop.
#    Name it lowest(stock). (Repeat: min with a key and a default)
def lowest(stock: dict[str, int]) -> str | None:
    return min(stock, key=lambda k: stock[k], default=None)


assert (got := lowest({"pen": 4, "ink": 1, "pad": 7})) == "ink", f"{got=}"
assert (got := lowest({"pen": 0})) == "pen", f"{got=}"
assert (got := lowest({})) is None, f"{got=}"


# 3. Return the names whose balance is at least the limit, highest balance first, ties A to Z.
#    One call to sorted with a key, unpack .items(), no reverse=True.
#    Name it at_limit(balances, limit). (Repeat: boundary wording, sort keys with a tie-break)
def at_limit(balances: dict[str, int], limit: int) -> list[str]:
    return sorted([k for k in balances if balances[k] >= limit], key=lambda b: (-balances[b], b))


balances = {"ben": 50, "cy": 49, "bea": 50, "al": 80}
assert (got := at_limit(balances, 50)) == ["al", "bea", "ben"], f"{got=}"
assert (got := at_limit(balances, 81)) == [], f"{got=}"
assert (got := at_limit({}, 0)) == [], f"{got=}"


# 4. Replay page visits and keep only the `capacity` most recent distinct pages.
#    Visiting a page again makes it the newest. Over capacity: drop the oldest.
#    Return the pages oldest to newest. Use OrderedDict: move_to_end and popitem(last=False).
#    Name it keep_recent(visits, capacity). (New: OrderedDict, the core of an LRU cache)
def keep_recent(visits: list[str], capacity: int) -> list[str]:
    od: OrderedDict[str, None] = OrderedDict()
    for v in visits:
        od[v] = None
        od.move_to_end(v)
        if len(od) > capacity:
            od.popitem(last=False)
    return list(od)


assert (got := keep_recent(["a", "b", "c", "a", "d"], 3)) == ["c", "a", "d"], f"{got=}"
assert (got := keep_recent(["a", "b", "a"], 2)) == ["b", "a"], f"{got=}"
assert (got := keep_recent(["a", "a", "a"], 2)) == ["a"], f"{got=}"
assert (got := keep_recent([], 2)) == [], f"{got=}"
assert (got := keep_recent(["a", "b"], 0)) == [], f"{got=}"


# 5. Make a dataclass Cart with fields owner (str) and items (list[str], empty by default).
#    Every Cart gets its own list. Add a method add(item) that appends to items.
#    Use field with default_factory from dataclasses.
#    (New: field(default_factory=...), a method on a dataclass)
@dataclass
class Cart:
    owner: str
    items: list[str] = field(default_factory=list)

    def add(self, item: str):
        self.items.append(item)


a, b = Cart("al"), Cart("bo")
a.add("pen")
a.add("ink")
assert (got := a.items) == ["pen", "ink"], f"{got=}"
assert (got := b.items) == [], f"each Cart needs its own list, {got=}"
assert (got := Cart("cy", ["pad"]).items) == ["pad"], f"{got=}"
assert (got := repr(Cart("cy"))) == "Cart(owner='cy', items=[])", f"{got=}"
