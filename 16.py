with open('16.txt') as f:
    lines = [a.replace('\n', '') for a in f.readlines()]


def validate(ticket, fields):
    for i, t in enumerate(ticket):
        valid = False
        for f in fields:
            if fields[f][0] <= t <= fields[f][1] or fields[f][2] <= t <= fields[f][3]:
                valid = True
                break
        if not valid:
            return t
    return 0


my_ticket, fields, nearby = [], {}, []
t = None
for line in lines:
    if ':' in line:
        if line in ('your ticket:', 'nearby tickets:'):
            t = line
        else:
            t, r = line.split(': ')
            r = r.split(' or ')
            a, b = r[0].split('-')
            c, d = r[1].split('-')
            fields[t] = (int(a), int(b), int(c), int(d))
            t = None
    elif t == 'your ticket:':
        my_ticket = [int(a) for a in line.split(',')]
        t = None
    elif t == 'nearby tickets:':
        ticket = [int(a) for a in line.split(',')]
        nearby.append(ticket)

answers = sum([validate(t, fields) for t in nearby])
print(answers)  # 22000
assert 22000 == answers

# remove invalid tickets
for ticket in nearby:
    if validate(ticket, fields) != 0:
        nearby.remove(ticket)

solutions = {}
for field in fields:
    solutions[field] = []

for i in range(len(fields)):
    for field in fields:
        ok = True
        for ticket in nearby:
            t = ticket[i]
            a, b, c, d = fields[field]

            if a <= t <= b or c <= t <= d:
                continue
            ok = False
            break
        if ok:
            solutions[field].append(i)

answers = []
while len(solutions) > 0:
    for solution in solutions:
        if len(solutions[solution]) == 1:
            value = solutions[solution][0]
            answers.append((solution, value))
            for s in solutions:
                if value in solutions[s]:
                    solutions[s].remove(value)
            break
    solutions.pop(solution)

result = 1
for field, value in answers:
    if str(field).startswith('departure'):
        result *= my_ticket[value]
print(result)  # 410460648673
assert 410460648673 == result
