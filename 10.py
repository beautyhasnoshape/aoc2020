with open("10.txt") as f:
    lines = sorted([0] + [int(a) for a in f.readlines()])  # add 0 as a starting node

adapters = [a for a in lines]
last, count_one, count_three = -1, 0, 1  # last node with distance 3 considered
for curr in adapters:
    if last != -1:
        if curr - last == 1:
            count_one += 1
        elif curr - last == 3:
            count_three += 1
    last = curr

print(count_one * count_three)  # 2176
assert 2176 == count_one * count_three


def traverse(l, idx):
    if idx == len(l) - 1:
        return 1
    s = 0
    for shift in range(1, 4):
        if idx + shift >= len(l):
            break
        if l[idx + shift] - l[idx] <= 3:
            s += traverse(l, idx + shift)
    return s


adapters = [a for a in lines]
start, result = 0, 1
for stop in range(1, len(adapters)):
    if stop == len(adapters) - 1 or adapters[stop] - adapters[stop - 1] == 3:
        d = 1 if stop == len(adapters) - 1 else 0
        variants = traverse(adapters[start:stop + d], 0)
        # print('subset', adapters[start:stop + d], 'has', variants, 'variants')
        result *= variants
        start = stop

print(result)  # 18512297918464
assert 18512297918464 == result
