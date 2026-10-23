# Key-value store with expiry
# Stateful implementation, step 1 (classic). Timebox 45 min. No AI, no lookups.
# Style: Option 1 (decided 2026-10-22): walrus unwrapping, early returns,
# keyword-only arguments, names that read like a sentence.
#
# Build a class KVStore that keeps string values under string keys.
# There is no real clock: every call gets the current time as `now`
# (whole seconds), and `now` never goes backwards.
#
# Part 1
#   set(key, value, *, now)     store value under key, replacing any old value
#   get(key, *, now)            the value, or None if the key is missing
#   delete(key, *, now)         remove the key: True if it was there, False if not
#
# Part 2: add expiry without breaking Part 1
#   set(key, value, *, now, ttl=None)
#       ttl is a number of seconds. None means the key never expires.
#       A key set at time t with ttl d is alive while now < t + d, and gone from t + d on.
#       Setting a key again replaces its expiry too (a set without ttl never expires).
#   get and delete treat an expired key as missing.
#   keys(*, now)                the live keys, A to Z
#
# The asserts are at the bottom, one block per part. Part 2's fail until Part 2 exists.
# When both pass: time and space for each method, out loud, then follow-up questions.

from dataclasses import dataclass


class KVStore:
    @dataclass(kw_only=True, frozen=True, slots=True)
    class Value:
        value: str
        expiration: int | None

    _store: dict[str, Value]

    def __init__(self) -> None:
        self._store = {}

    def set(self, key: str, value: str, *, now: int, ttl: int | None = None) -> None:
        self._store[key] = self.Value(
            value=value, expiration=(now + ttl) if ttl is not None else None
        )

    def get(self, key: str, *, now: int) -> str | None:
        self._expire_if_needed(key, now)
        return result.value if (result := self._store.get(key)) is not None else None

    def delete(self, key: str, *, now: int) -> bool:
        self._expire_if_needed(key, now)
        return self._store.pop(key, None) is not None

    def _expire_if_needed(self, key: str, now: int) -> None:
        if self._is_expired(self._store.get(key), now):
            del self._store[key]

    def _is_expired(self, val: Value | None, now: int) -> bool:
        return val is not None and val.expiration is not None and (now >= val.expiration)

    def keys(self, *, now: int) -> list[str]:
        expired_keys = [k for k, v in self._store.items() if self._is_expired(v, now)]
        for k in expired_keys:
            del self._store[k]
        return sorted(self._store)


# ---- Part 1 ----
s = KVStore()
assert (got := s.get("a", now=0)) is None, f"{got=}"
s.set("a", "1", now=1)
assert (got := s.get("a", now=2)) == "1", f"{got=}"
s.set("a", "2", now=3)  # replaces the old value
assert (got := s.get("a", now=4)) == "2", f"{got=}"
assert (got := s.delete("a", now=5)) is True, f"{got=}"
assert (got := s.get("a", now=6)) is None, f"{got=}"
assert (got := s.delete("a", now=7)) is False, f"{got=}"
s.set("b", "", now=8)  # an empty string is a value, not "missing"
assert (got := s.get("b", now=9)) == "", f"{got=}"
assert (got := s.delete("b", now=10)) is True, f"{got=}"

# ---- Part 2 ----
s = KVStore()
s.set("a", "1", now=10, ttl=5)
assert (got := s.get("a", now=14)) == "1", f"alive while now < 15, {got=}"
assert (got := s.get("a", now=15)) is None, f"gone from 10 + 5 on, {got=}"
assert (got := s.delete("a", now=16)) is False, f"expired counts as missing, {got=}"
s.set("b", "1", now=0)  # no ttl: never expires
assert (got := s.get("b", now=10**9)) == "1", f"{got=}"
s.set("c", "1", now=0, ttl=10)
s.set("c", "2", now=5)  # set again without ttl: the expiry is gone
assert (got := s.get("c", now=100)) == "2", f"{got=}"
s.set("d", "1", now=0)
s.set("d", "2", now=1, ttl=3)  # set again with ttl: now it expires at 4
assert (got := s.get("d", now=3)) == "2", f"{got=}"
assert (got := s.get("d", now=4)) is None, f"{got=}"
s.set("z", "1", now=20, ttl=0)  # ttl 0 is never alive
assert (got := s.get("z", now=20)) is None, f"{got=}"
s.set("e", "1", now=20, ttl=1)
assert (got := s.keys(now=20)) == ["b", "c", "e"], f"{got=}"
assert (got := s.keys(now=21)) == ["b", "c"], f"{got=}"
s.set("a", "back", now=22)  # an expired key can be set again
assert (got := s.keys(now=22)) == ["a", "b", "c"], f"{got=}"
assert (got := s.delete("b", now=23)) is True, f"{got=}"
assert (got := s.keys(now=23)) == ["a", "c"], f"{got=}"
assert (got := KVStore().keys(now=0)) == [], f"{got=}"
t = KVStore()
t.set("y", "1", now=0, ttl=0)  # expires at time 0: still a real expiry
assert (got := t.get("y", now=0)) is None, f"{got=}"
