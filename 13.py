with open("13.txt") as f:
    lines = [a for a in f.readlines()]
    timestamp = int(lines[0])
    buses = [int(a) for a in lines[1].replace('\n', '').split(',') if a != 'x']

t, starts = timestamp, []
for bus in buses:
    starts.append((timestamp // bus) * bus + bus)

bus = buses[starts.index(min(starts))]
result = bus * (min(starts) - timestamp)
print(result)  # 156
assert 156 == result

start = int(lines[0])
buses = ["x" if x == "x" else int(x) for x in lines[1].split(",")]

buses = [41, 37, 971, 17, 13, 23, 29, 487, 19]
delay = [ 0, 35,  41, 58, 59, 64, 70, 72,  91]


# hint: use Chinese Remainder Theorem to solve congruence in Part 2
# x ===  0 (mod 41)  =  41 * a
# x === 35 (mod 37)  =  37 * b + 35
# x === 41 (mod 971) = 971 * c + 41
# x === 58 (mod 17)  =  17 * d + 58
# x === 59 (mod 13)  =  13 * e + 59
# x === 64 (mod 23)  =  23 * f + 64
# x === 70 (mod 29)  =  29 * g + 70
# x === 72 (mod 487) = 487 * h + 72
# x === 91 (mod 19)  =  19 * i + 91
from sympy.ntheory.modular import solve_congruence
bus_times = list(map(lambda a, b: (-b, a), buses, delay))

print(solve_congruence(*bus_times))
