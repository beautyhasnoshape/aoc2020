with open("08.txt") as f:
    instructions = [(a.split(' ')[0], int(a.split(' ')[1].replace('\n', ''))) for a in f.readlines()]

size = len(instructions)
commands = {
    'jmp': lambda arg, idx, acc: (idx + arg, acc),
    'acc': lambda arg, idx, acc: (idx + 1, acc + arg),
    'nop': lambda arg, idx, acc: (idx + 1, acc)
}


def execute():
    idx, result = 0, 0
    visited, terminated = [], False

    while idx != size:
        idx = (idx + size) % size
        if idx in visited:
            terminated = True
            break
        visited.append(idx)

        instr, arg = instructions[idx]
        idx, result = commands[instr](arg, idx, result)

    return result, terminated


result, terminated = execute()
print(result)
assert 2051 == result


def swap_instruction(idx, swapping):
    instr, arg = instructions[idx]
    if instr in swapping:
        instructions[idx] = (swapping[(swapping.index(instr) + 1) % 2], arg)
        return True

    return False


result = 0
swapping = ('jmp', 'nop')
for i in range(size):
    swapped = swap_instruction(i, swapping)
    if not swapped:
        continue
    result, terminated = execute()
    swap_instruction(i, swapping)

    if not terminated:
        break

print(result)
assert 2304 == result
