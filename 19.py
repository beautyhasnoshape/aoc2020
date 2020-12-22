import regex as re

with open('19.txt') as f:
    input_a, input_b = f.read().split('\n\n')

all_rules = {
    rule_id: t.split() for rule_id, t in [x.split(': ') for x in input_a.split('\n')]
}
texts = input_b.split('\n')


def traverse(token: str, rules: {}, cache={}) -> str:
    if token in cache:
        return cache[token]
    elif token in ('"a"', '"b"'):
        return token[1]
    elif token == '|':
        return '|'
    else:
        answer = '(' + ''.join(traverse(rule, rules, cache) for rule in rules[token]) + ')'
        cache[token] = answer
        return answer


result = sum([1 if re.match('^' + traverse('0', all_rules) + '$', txt) else 0 for txt in texts])
print(result)  # 265
assert 265 == result

repeats = 6  # experiment with the number of pattern repetition until the result value does not increase anymore
all_rules['8'] = '| '.join('42 ' * i for i in range(1, repeats)).split()
all_rules['11'] = '| '.join('42 ' * i + '31 ' * i for i in range(1, repeats)).split()

result = sum([1 if re.match('^' + traverse('0', all_rules, cache={}) + '$', txt) else 0 for txt in texts])
print(result)  # 394
assert 394 == result
