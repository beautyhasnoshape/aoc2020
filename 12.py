import math

with open("12.txt") as f:
    lines = [a for a in f.readlines()]

directions = ('N', 'E', 'S', 'W')
moves = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

direction, position = 'E', (0, 0)
for line in lines:
    action, value = line[0], int(line[1:])
    if action in ('N', 'E', 'S', 'W'):
        position = (position[0] + moves[action][0] * value, position[1] + moves[action][1] * value)
    elif action in ('F'):
        position = (position[0] + moves[direction][0] * value, position[1] + moves[direction][1] * value)
    elif action in ('L'):
        direction = directions[(directions.index(direction) - (value // 90) + 4) % 4]
    elif action in ('R'):
        direction = directions[(directions.index(direction) + (value // 90) + 4) % 4]

result = abs(position[0]) + abs(position[1])
print(result)  # 1603
assert 1603 == result


def rotate(point, angle):
    px, py = point
    qx = math.cos(angle) * px - math.sin(angle) * py
    qy = math.sin(angle) * px + math.cos(angle) * py

    return round(qx), round(qy)


direction, position, waypoint = 'E', (0, 0), (10, 1)
for line in lines:
    action, value = line[0], int(line[1:])
    if action in ('N', 'E', 'S', 'W'):
        waypoint = (waypoint[0] + moves[action][0] * value, waypoint[1] + moves[action][1] * value)
    elif action in 'F':
        for _ in range(value):
            position = (position[0] + waypoint[0], position[1] + waypoint[1])
    elif action in 'L':
        waypoint = rotate(waypoint, math.radians(value))
    elif action in 'R':
        waypoint = rotate(waypoint, math.radians(-value))

result = abs(position[0]) + abs(position[1])
print(result)  # 52866
assert 52866 == result

