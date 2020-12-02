import itertools

with open("01.txt") as f:
    numbers = set([int(a) for a in f.readlines()])

    for p in numbers:
        if 2020-p in numbers:
            print(p*(2020-p))
            assert 55776 == p*(2020-p)
            break

    for (a, b) in itertools.combinations(numbers, 2):
        if 2020-a-b in numbers:
            print(a*b*(2020-a-b))
            assert 223162626 == a*b*(2020-a-b)
            break

