with open("09.txt") as f:
    numbers = [int(a) for a in f.readlines()]


def is_valid(x, subset):
    for i in range(len(subset)-1):
        for j in range(i+1, len(subset)):
            s = subset[i] + subset[j]
            if x == s:
                return True
    return False


for idx in range(25, len(numbers)):
    n = numbers[idx]
    subset = numbers[idx-25: idx]
    if not is_valid(n, subset):
        result = n
        break

print(result)  # 177777905
assert 177777905 == result


for i in range(25, len(numbers)-1):
    s = 0
    for j in range(i, len(numbers)):
        s += numbers[j]
        if s == result:
            subset = numbers[i:j+1]
            result = min(subset) + max(subset)
            break
        if s > result:
            break

print(result)  # 23463012
assert 23463012 == result
