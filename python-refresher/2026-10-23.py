# Day 8 (2026-10-23): 3 repeats + 2 new. Write your own imports and signatures.
# Theme: the Python behind today's exercise (strings and parsing).
# Style: Option 1 (walrus unwrapping, early returns, keyword-only labels).


# 1. Return the k most common words, highest count first, ties A to Z.
#    Words are split on any whitespace and compared in lowercase.
#    Counter, one call to sorted with a key, no reverse=True. k is keyword-only.
#    Name it top_words(text, *, k). (Repeat: Counter + split(), whole-value tie-break)
import re
from collections import Counter


def top_words(text: str, *, k: int) -> list[str]:
    c = Counter(sorted(text.lower().split()))
    return [t for t, _ in c.most_common(k)]


assert (got := top_words("b a b c a b", k=2)) == ["b", "a"], f"{got=}"
assert (got := top_words("pear peak pear peak fig", k=2)) == ["peak", "pear"], f"{got=}"
assert (got := top_words("The the THE cat", k=1)) == ["the"], f"{got=}"
assert (got := top_words("  a\n\tb  a ", k=5)) == ["a", "b"], f"{got=}"
assert (got := top_words("", k=3)) == [], f"{got=}"


# 2. Turn (name, price) pairs into receipt lines joined by newlines, no trailing newline.
#    Each line: name left-aligned in 8 characters, then price right-aligned in 8
#    with 2 decimals. Long names are never cut. One f-string inside a comprehension.
#    Name it receipt(items). (Repeat: f-string alignment and specs, join, unpacking)
def receipt(items: list[tuple[str, float]]) -> str:
    return "\n".join([f"{name:<8}{price:>8.2f}" for name, price in items])


assert (got := receipt([("tea", 3.5), ("scone", 12)])) == "tea         3.50\nscone      12.00", (
    f"{got=}"
)
assert (got := receipt([("croissant", 2)])) == "croissant    2.00", f"{got=}"
assert (got := receipt([])) == "", f"{got=}"


# 3. Replace every character except the last 4 with "*".
#    Strings of 4 or fewer characters come back unchanged. No if, no loop.
#    Name it mask(card). (Repeat: negative slicing, string repetition)
def mask(card: str) -> str:
    return "*" * len(card[:-4]) + card[-4:]


assert (got := mask("1234567812345678")) == "************5678", f"{got=}"
assert (got := mask("12345")) == "*2345", f"{got=}"
assert (got := mask("1234")) == "1234", f"{got=}"
assert (got := mask("12")) == "12", f"{got=}"
assert (got := mask("")) == "", f"{got=}"


# 4. Split "key=value" at the first "=" and strip spaces around both parts.
#    Return None when there is no "=" or the key is empty. An empty value is fine.
#    Use str.partition, guard with early returns, no split, no indexing.
#    Name it parse_pair(text). (New: partition, guard-style early return)
def parse_pair(text: str) -> tuple[str, str] | None:
    prefix, separator, suffix = (val.strip() for val in text.partition("="))
    if not prefix or not separator:
        return None
    return (prefix, suffix)


assert (got := parse_pair("a=b")) == ("a", "b"), f"{got=}"
assert (got := parse_pair(" name = Ada Lovelace ")) == ("name", "Ada Lovelace"), f"{got=}"
assert (got := parse_pair("url=x?a=1")) == ("url", "x?a=1"), f"{got=}"
assert (got := parse_pair("a=")) == ("a", ""), f"{got=}"
assert (got := parse_pair("novalue")) is None, f"{got=}"
assert (got := parse_pair(" = x")) is None, f"{got=}"
assert (got := parse_pair("")) is None, f"{got=}"


# 5. Parse a log line "HH:MM:SS LEVEL message" into a dict with keys time, level, msg.
#    Time is two digits each, level is uppercase letters only, single spaces between
#    the three parts, the message is the rest and can't be empty. Anything else: None.
#    Use re.fullmatch with named groups, written (?P<name>...), and unwrap the match
#    with a walrus. Name it parse_log(line). (New: re named groups, walrus unwrapping)
def parse_log(line: str) -> dict[str, str] | None:
    pattern = r"^(?P<time>\d{2}:\d{2}:\d{2})\s(?P<level>[A-Z]+)\s(?P<msg>.+)$"
    if match := re.fullmatch(pattern, line, flags=0):
        return {
            "time": match.group("time"),
            "level": match.group("level"),
            "msg": match.group("msg"),
        }

    return None


assert (got := parse_log("09:15:02 ERROR disk full")) == {
    "time": "09:15:02",
    "level": "ERROR",
    "msg": "disk full",
}, f"{got=}"
assert (got := parse_log("23:59:59 INFO a=1 b=2")) == {
    "time": "23:59:59",
    "level": "INFO",
    "msg": "a=1 b=2",
}, f"{got=}"
assert (got := parse_log("9:15:02 ERROR x")) is None, f"{got=}"
assert (got := parse_log("09:15:02 error x")) is None, f"{got=}"
assert (got := parse_log("09:15:02 ERROR")) is None, f"{got=}"
assert (got := parse_log("x 09:15:02 ERROR disk")) is None, f"{got=}"
