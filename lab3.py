import re

opers = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
}

number = re.compile(r"([0-9]+(\.[0-9]+)*|[a-z])")
post_func = re.compile(r"[!]")
pre_func = re.compile("(sin|cos)")

def infix_to_rpn(string):
    stack = []
    out = []

    expresion = [token for token in string.split(' ')]

    while len(expresion) > 0:
        token = expresion.pop(0)
        if number.search(token) or post_func.search(token):
            out.append(token)
        elif pre_func.search(token):
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                out.append(stack.pop())
            stack.pop()
        elif opers[token] != None:
            while len(stack) > 0 and opers.get(token) != None and opers.get(stack[- 1]) != None and (pre_func.search(stack[-1]) or opers[stack[-1]] >= opers[token]):
                out.append(stack.pop())
            stack.append(token)

    while len(stack) > 0:
        out.append(stack.pop())

    res = ''
    for i in out:
        res += f"{i} "
    return res


print(infix_to_rpn(input()))