with open('15.txt') as f:
    lines = [int(a) for a in f.readline().replace('\n', '').split(',')]


def solve(numbers, count):
    history = {}
    for idx, a in enumerate(numbers):
        history[a] = idx

    next = 0
    for i in range(len(numbers), count - 1):
        if next not in history:
            history[next] = i
            next = 0
        else:
            last = next
            next = i - history[next]
            history[last] = i

    return next


result = solve(lines, 2020)
print(result)  # 1280
assert 1280 == result

result = solve([2, 15, 0, 9, 1, 20], 30000000)
print(result)  # 651639
assert 651639 == result
