from numba import njit
with open('25.txt') as f:
    lines = [line.strip() for line in f.readlines()]

cards_key, doors_key = int(lines[0]), int(lines[1])


@njit
def calculate_size(subject, key):
    value, size = 1, 0
    while value != key:
        size += 1
        value *= subject
        value %= 20201227
    return size


@njit
def calculate(subject, size):
    value = 1
    for _ in range(size):
        value *= subject
        value %= 20201227
    return value


size = calculate_size(7, cards_key)
result = calculate(doors_key, size)

print(result)  # 19924389
assert 19924389 == result
