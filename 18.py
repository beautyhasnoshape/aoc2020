with open('18.txt') as f:
    lines = [l.strip() for l in f.readlines()]


def convert_to_rpn(expression: str, ops: {}) -> []:  # reversed polish notation
    # use shunting-yard algorithm
    stack, out = [], []
    for token in expression:
        if '0' <= token <= '9':
            out.append(int(token))
        elif '(' == token:
            stack.append(token)
        elif ')' == token:
            t = stack.pop()
            while t != '(':
                out.append(t)
                t = stack.pop()
        elif token in ops:
            if len(stack) == 0 or stack[-1] in ops and ops[stack[-1]][1] < ops[token][1]:
                stack.append(token)
            else:
                while len(stack) > 0 and stack[-1] in ops and ops[stack[-1]][1] >= ops[token][1]:
                    out.append(stack.pop())
                stack.append(token)

    while len(stack) > 0:
        out.append(stack.pop())

    return out


def eval_rpn(rpn: [], ops: {}) -> int:
    stack = []
    for token in rpn:
        if token in ops:
            stack.append(ops[token][0](stack.pop(), stack.pop()))
        else:
            stack.append(token)

    return stack[0]


def evaluate(expression: str, ops: {}) -> int:
    return eval_rpn(convert_to_rpn(expression, ops), ops)


operators = {
    '+': (lambda a, b: a + b, 0),
    '*': (lambda a, b: a * b, 0)
}
result = sum([evaluate(line, operators) for line in lines])
print(result)  # 4297397455886
assert 4297397455886 == result


operators = {
    '+': (lambda a, b: a + b, 1),
    '*': (lambda a, b: a * b, 0)
}
result = sum([evaluate(line, operators) for line in lines])
print(result)  # 93000656194428
assert 93000656194428 == result


# tests
operators = {
    '+': (lambda a, b: a + b, 0),
    '×': (lambda a, b: a * b, 1)
}
rpn = convert_to_rpn('1 + 2 × (3 × 4 + 5 × 6)', operators)
val = eval_rpn(rpn, operators)
assert [1, 2, 3, 4, '×', 5, 6, '×', '+', '×', '+'] == rpn
assert 85 == val
assert 85 == evaluate('1 + 2 × (3 × 4 + 5 × 6)', operators)
