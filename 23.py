def solve(moves: [], repetitions: int) -> {}:
    current, size, max_value = moves[0], len(moves), max(moves)
    circle = {
        int(value): moves[(id + 1) % size] for id, value in enumerate(moves)
    }

    for _ in range(repetitions):
        removed = (circle[current], circle[circle[current]], circle[circle[circle[current]]])
        dest = current - 1
        if dest < 1:
            dest = max_value
        while dest in removed:
            dest -= 1
            if dest < 1:
                dest = max_value
        if dest < 1:
            dest = max_value

        circle[current] = circle[removed[2]]
        current = circle[current]

        circle[removed[2]] = circle[dest]
        circle[dest] = removed[0]

    return circle


moves = [4, 5, 9, 6, 7, 2, 8, 1, 3]
circle = solve(moves, 100)

node, result = 1, ''
while circle[node] != 1:
    result += str(circle[node])
    node = circle[node]
print(result)  # 68245739
assert '68245739' == result

moves = [4, 5, 9, 6, 7, 2, 8, 1, 3] + [int(a) for a in range(10, 1_000_001)]
circle = solve(moves, 10_000_000)

result = circle[1] * circle[circle[1]]
print(result)  # 219634632000
assert 219634632000 == result
