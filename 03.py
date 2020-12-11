from functools import reduce

with open("03.txt") as f:
    lines = [a.replace('\n', '') for a in f.readlines()]


def solve(grid: [], dx: int, dy: int) -> int:
    count, x, y = 0, 0, 0
    while y + dy < len(grid):
        x = (x + dx) % len(grid[0])
        y = (y + dy)
        count += 1 if grid[y][x] == '#' else 0

    return count


result = solve(lines, 3, 1)
print(result)  # 259
assert 259 == result

result = solve(lines, 1, 1) * solve(lines, 3, 1) * solve(lines, 5, 1) * solve(lines, 7, 1) * solve(lines, 1, 2)
print(result)  # 2224913600
assert 2224913600 == result

# using lambda and reduce
assert 2224913600 == reduce(lambda x, y: x * y, [solve(lines, a, b) for a, b in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]])




