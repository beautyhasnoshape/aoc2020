with open('17.txt') as f:
    lines = [a.strip() for a in f.readlines()]

domain = (-1, 0, 1)  # values to generate shifts for surrounding cells

# contains active (x, y, z) cells only
grid = set([(x, y, 0) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '#'])

for step in range(6):
    new_grid = set()
    space = range(-step - 1, len(lines[0]) + step + 1)  # grid is growing each direction by 1 with every step
    for x, y, z in [(x, y, z) for x in space for y in space for z in space]:
        count = 0
        for dx, dy, dz in [(a, b, c) for a in domain for b in domain for c in domain
                           if (a, b, c) != (0, 0, 0)]:
            if (x + dx, y + dy, z + dz) in grid:  # neighbour in the grid
                count += 1
        if (x, y, z) in grid and count in (2, 3):  # only cells inside the grid (ones remaining active)
            new_grid.add((x, y, z))
        elif (x, y, z) not in grid and count == 3:  # cells outside the grid too (passive turning into active)
            new_grid.add((x, y, z))
    grid = new_grid

result = len(grid)
print(result)  # 424
assert 424 == result


# contains active (x, y, z, w) cells only
grid = set([(x, y, 0, 0) for y, line in enumerate(lines) for x, c in enumerate(line) if c == '#'])

for step in range(6):
    new_grid = set()
    space = range(-step - 1, len(lines[0]) + step + 1)  # grid is growing each direction by 1 with every step
    for x, y, z, w in [(x, y, z, w) for x in space for y in space for z in space for w in space]:
        count = 0
        for dx, dy, dz, dw in [(a, b, c, d) for a in domain for b in domain for c in domain for d in domain
                               if (a, b, c, d) != (0, 0, 0, 0)]:
            if (x + dx, y + dy, z + dz, w + dw) in grid:  # neighbour in the grid
                count += 1
        if (x, y, z, w) in grid and count in (2, 3):  # only cells inside the grid (ones remaining active)
            new_grid.add((x, y, z, w))
        elif (x, y, z, w) not in grid and count == 3:  # cells outside the grid too (passive turning into active)
            new_grid.add((x, y, z, w))
    grid = new_grid

result = len(grid)
print(result)  # 2460
assert 2460 == result
