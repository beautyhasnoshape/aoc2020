from functools import reduce

with open("11.txt") as f:
    lines = [a for a in f.readlines()]
directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]


def is_valid_position(seats: [], row: int, col: int) -> bool:
    return 0 <= row < len(seats) and 0 <= col < len(seats[0])


def is_seat_type(seats: [], row: int, col: int, type: str) -> bool:
    return is_valid_position(seats, row, col) and seats[row][col] == type


def count_adjacent_seats(seats: [], row: int, col: int, type: str='#') -> int:
    return sum(1 if is_seat_type(seats, row + d[0], col + d[1], type) else 0 for d in directions)


def count_seats(seats: [], type: str='#'):
    return sum(1 if seats[row][col] == type else 0 for col in range(len(seats[0])) for row in range(len(seats)))


def arrange(seats: []) -> []:
    count, new_seats = 0, []
    for row in range(len(seats)):
        new_row = []
        for col in range(len(seats[0])):
            occupied_adj_count = count_adjacent_seats(seats, row, col)
            if seats[row][col] == '#' and occupied_adj_count >= 4:
                new_row.append('L')
                count += 1
            elif seats[row][col] == 'L' and occupied_adj_count == 0:
                new_row.append('#')
                count += 1
            else:
                new_row.append(seats[row][col])
        new_seats.append(new_row)
    for row in range(len(seats)):
        seats[row] = new_seats[row]

    return count


def visible_count(seats: [], row: int, col: int, type: str) -> int:
    count, y, x = 0, row, col
    for d in directions:
        y, x = row + d[0], col + d[1]
        while is_valid_position(seats, y, x):
            if seats[y][x] == type:
                count += 1
                break
            elif seats[y][x] == 'L':
                break
            y, x = y + d[0], x + d[1]

    return count


def arrange2(seats: []) -> []:
    count, new_seats = 0, []
    for row in range(len(seats)):
        new_row = []
        for col in range(len(seats[0])):
            visible_adj_count = visible_count(seats, row, col, '#')
            if seats[row][col] == '#' and visible_adj_count >= 5:
                new_row.append('L')
                count += 1
            elif seats[row][col] == 'L' and visible_adj_count == 0:
                new_row.append('#')
                count += 1
            else:
                new_row.append(seats[row][col])
        new_seats.append(new_row)

    for row in range(len(seats)):
        seats[row] = new_seats[row]

    return count


count, seats = 1, [reduce(lambda a, b: a + b, line) for line in lines]
while count > 0:
    count = arrange(seats)

result = count_seats(seats)
print(result)  # 2273
assert 2273 == result


count, seats = 1, [reduce(lambda a, b: a + b, line) for line in lines]
while count > 0:
    count = arrange2(seats)

result = count_seats(seats)
print(result)  # 2064
assert 2064 == result
