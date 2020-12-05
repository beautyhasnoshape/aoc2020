import math

with open("05.txt") as f:
    lines = [a.replace('\n', '') for a in f.readlines()]


def calc_position(position):
    a, b, c, d = 0, 127, 0, 7
    for ch in position:
        if ch == 'F':
            b = math.floor((a + b) / 2)
        elif ch == 'B':
            a = math.ceil((a + b) / 2)
        elif ch == 'L':
            d = math.floor((c + d) / 2)
        elif ch == 'R':
            c = math.ceil((c + d) / 2)
    return a * 8 + c


ids = []
for line in lines:
    id = calc_position(line)
    ids.append(id)

print(max(ids))
assert 953 == max(ids)

for row in range(1, 126):
    for col in range(8):
        id = row * 8 + col
        if id not in ids and id - 1 in ids and id + 1 in ids:
            print(id)
            assert 615 == id
            break


def show_seats(ids):
    for row in range(127):
        a = ''
        for col in range(8):
            a += ' ' if row * 8 + col in ids else 'x'
        print(a, row)


# tests
assert 357 == calc_position('FBFBBFFRLR')
assert 567 == calc_position('BFFFBBFRRR')
assert 119 == calc_position('FFFBBBFRRR')
assert 820 == calc_position('BBFFBBFRLL')
