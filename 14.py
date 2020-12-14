import itertools
from functools import reduce

with open('14.txt') as f:
    lines = [a.replace('\n', '') for a in f.readlines()]

mask, register = None, {}
for line in lines:
    if line.startswith('mask'):
        mask = line.split(' = ')[1]
    else:
        idx = int(line.split('=')[0][4:-2])
        value = int(line.split('=')[1])

        b = str(bin(value))
        b = b.replace('0b', '0' * (36 - len(b) + 2))

        for i in range(len(mask)):
            if mask[i] in ('0', '1'):
                b = b[:i] + mask[i] + b[i + 1:]

        register[idx] = int(b, 2)

result = sum([int(register[idx]) for idx in register])
print(result)  # 8566770985168
assert 8566770985168 == result

mask, register = None, {}
for line in lines:
    b = None
    if line.startswith('mask'):
        mask = line.split(' = ')[1]
    else:
        idx = int(line.split('=')[0][4:-2])
        value = int(line.split('=')[1])

        b = str(bin(idx))  # address
        b = b.replace('0b', '0' * (36 - len(b) + 2))

        for i in range(len(mask)):
            if mask[i] == '0':
                pass
            elif mask[i] in ('1', 'X'):
                b = b[:i] + mask[i] + b[i + 1:]

        variants = itertools.product(('0', '1'), repeat=b.count('X'))
        for variant in variants:
            address = str(b)
            for a in variant:
                address = address.replace('X', a, 1)
            register[int(address, 2)] = value

result = sum([int(register[idx]) for idx in register])
print(result)  # 4832039794082
assert 4832039794082 == result
