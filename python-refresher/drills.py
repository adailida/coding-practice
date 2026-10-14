# from functools import reduce


def average(num1: float, num2: float) -> float:
    return (num1 + num2) / 2
    # return average(num1, num2)


print(average(num1=3, num2=4))


# Drill 2: list and for loop
def total(numbers: list[float]) -> float:
    # return sum(numbers)

    # return reduce(lambda acc, x: acc + x, numbers)

    result = 0

    for num in numbers:
        result += num
    return result


print(total([1, 2, 3.5]))


# Drill 3: enumerate
def index_of_max(numbers: list[float]) -> int:
    result = -1
    max_num = None

    for index, num in enumerate(numbers):
        if max_num is None or num > max_num:
            result = index
            max_num = num

    return result


print(index_of_max(numbers=[4, 9, 2]))


# Drill 4: zip
def dot(list1: list[float], list2: list[float]) -> float:
    result = 0

    for el1, el2 in zip(list1, list2, strict=True):
        result += el1 * el2

    return result


print(dot(list1=[1, 2, 3], list2=[4, 5, 6]))


# Drill 5: dictionaries
def count_votes(lst: list[str]) -> dict[str, int]:
    result = {}
    for s in lst:
        # result[s] = result[s] + 1 if s in result else 1
        result[s] = 1 + result.get(s, 0)
    return result


print(count_votes(lst=["a", "b", "a"]))


# Drill 6: sorted and max with a key
def rank(d: dict[str, float]) -> list[str]:
    # return list(dict(sorted(d.items(), key=lambda item: item[1], reverse=True)).keys())
    # return [i[0] for i in sorted(d.items(), key=lambda item: item[1], reverse=True)]
    return sorted(d, key=d.get, reverse=True)


def best(d: dict[str, float]) -> str:
    return max(d, key=d.get)


print(rank(d={"ann": 2.5, "bob": 4.0, "cy": 3.0}))
print(best(d={"ann": 2.5, "bob": 4.0, "cy": 3.0}))


# Drill 7: List comprehensions
def normalize(lst: list[float]) -> list[float]:
    total = sum(lst)
    return [val / total for val in lst]


print(normalize(lst=[2, 3, 5]))


def above(dct: dict[str, float], threshold: float) -> list[str]:
    return [key for key in dct if dct[key] > threshold]


print(above(dct={"ann": 2.5, "bob": 4.0, "cy": 3.0}, threshold=2.9))
# Drill 8: floats, integer division, rounding
# print(0.1 + 0.2 == 0.3) False
# print(7 // 2) 3
# print(-7 // 2) -4
# print(7 % 2) 1
# print(int(2.9)) 2
# print(int(-2.9)) -2
# print(round(2.5)) 2
# print(round(3.5)) 4
print(0.1 + 0.2 == 0.3)
print(7 // 2)
print(-7 // 2)
print(7 % 2)
print(int(2.9))
print(int(-2.9))
print(round(2.5))
print(round(3.5))


def almost_equal(n1: float, n2: float, tol=1e-9) -> bool:
    return abs(n1 - n2) < tol


print(almost_equal(0.1 + 0.2, 0.3))


# Drill 9: while loop
def years_to_double(rate: float, default_balance=1.0, target_balance=2.0) -> int:
    if rate <= 0:
        raise ValueError("error!")

    balance = default_balance
    result = 0

    while balance < target_balance:
        balance *= 1 + rate
        result += 1

    return result


# Drill 10: assert
assert total([]) == 0
assert almost_equal(dot(list1=[1.1], list2=[2]), 2.2)
print("all drills pass")
