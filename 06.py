with open("06.txt") as f:
    lines = [a.replace('\n', '') for a in f.readlines()]

    groups, idx = [[]], 0
    for line in lines:
        if len(line) == 0:
            idx += 1
            groups.append([])
        else:
            groups[idx].append(line)

count, s = 0, ''
for group in groups:
    for a in group:
        s += a
    count += len(set(s))
    s = ''

print(count)  # 6662
assert 6662 == count


count = 0
for group in groups:
    s = group[0]
    for a in group:
        s = set(s).intersection(a)
    count += len(s)

print(count)  # 3382
assert 3382 == count
