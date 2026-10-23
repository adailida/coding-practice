# Decode string
# Strings and parsing, step 1 (classic). Timebox 45 min. No AI, no lookups.
# Style: Option 1 (walrus unwrapping, early returns, names that read like a sentence).
#
# Write decode(encoded) that expands a compressed string.
#   k[part] means part repeated k times. Parts can nest: 2[a3[b]] is abbbabbb.
#   Plain letters outside brackets stay as they are.
#   k is a positive whole number and can have more than one digit (12[a]).
#
# You can assume the input is valid: lowercase letters, digits only as repeat
# counts, every count is followed by "[", and every bracket is closed.
#
# The asserts are at the bottom.
# When they pass: time and space out loud, then follow-up questions.


def decode(encoded: str) -> str:
    return _decode(encoded, 0)[0]


def _decode(encoded: str, i: int) -> tuple[str, int]:
    decoded = ""
    count = ""
    while i < len(encoded):
        match encoded[i]:
            case char if char.isdigit():
                count += char
            case "[":
                decoded_substring, i = _decode(encoded, i + 1)
                decoded += int(count) * decoded_substring
                count = ""
            case "]":
                return decoded, i
            case char:
                decoded += char
        i += 1

    return decoded, i


assert (got := decode("3[a]2[bc]")) == "aaabcbc", f"{got=}"
assert (got := decode("3[a2[c]]")) == "accaccacc", f"{got=}"
assert (got := decode("2[abc]3[cd]ef")) == "abcabccdcdcdef", f"{got=}"
assert (got := decode("ab2[c]d")) == "abccd", f"{got=}"
assert (got := decode("2[a2[b]c]")) == "abbcabbc", f"{got=}"
assert (got := decode("3[ab2[c]]")) == "abccabccabcc", f"{got=}"
assert (got := decode("2[2[2[a]]]")) == "aaaaaaaa", f"{got=}"
assert (got := decode("10[a]")) == "aaaaaaaaaa", f"{got=}"
assert (got := decode("2[12[x]y]")) == "xxxxxxxxxxxxyxxxxxxxxxxxxy", f"{got=}"
assert (got := decode("1[a]")) == "a", f"{got=}"
assert (got := decode("abc")) == "abc", f"{got=}"
assert (got := decode("")) == "", f"{got=}"
