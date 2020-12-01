import itertools

with open("01.txt") as f:
    numbers = [int(a) for a in f.readlines()]

    for p in itertools.combinations(numbers, 2):
        if sum(p) == 2020:
            print(p[0]*p[1])

    for p in itertools.combinations(numbers, 3):
        if sum(p) == 2020:
            print(p[0]*p[1]*p[2])
