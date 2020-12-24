import regex as re

with open('24.txt') as f:
    lines = [line.strip() for line in f.readlines()]

# for hexagon coordinates see https://www.redblobgames.com/grids/hexagons/#neighbors-axial
dirs = {
    'e': (2, 0), 'se': (1, 1), 'sw': (-1, 1), 'w': (-2, 0), 'nw': (-1, -1), 'ne': (1, -1)
}

ref = (0, 0)
grid = []

for line in lines:
    queue = re.findall('(ne|nw|se|sw|w|e)', line)
    cell = ref
    for d in queue:
        cell = (cell[0] + dirs[d][0], cell[1] + dirs[d][1])

    if cell in grid:
        grid.remove(cell)
    else:
        grid.append(cell)


result = len(grid)
print(result)  # 307
assert 307 == result

for _ in range(100):
    neighbours = {}

    for (p, q) in grid:
        shifts = {
            (p + dp, q + dq) for (dp, dq) in dirs.values()
        }
        for n in shifts:
            if n not in neighbours:
                neighbours[n] = 1
            else:
                neighbours[n] += 1

    black = set()
    for n in neighbours:
        if n not in grid and neighbours[n] == 2:
            black.add(n)
        elif n in grid and neighbours[n] in (1, 2):
            black.add(n)

    grid = black

result = len(grid)
print(result)  # 3787
assert 3787 == result
