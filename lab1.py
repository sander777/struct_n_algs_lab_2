import re

RED = '\033[1;31m'
NC = '\033[0;37m'


class Bracket:
    def __init__(self, c):
        self.color = RED
        self.c = c


stack = []
brackets = list(map(lambda x: Bracket(x), [char for char in input()]))

OPEN_BRACKETS = re.compile(r"[\[\(\{]")

pairs = {
    '{': '}',
    '[': ']',
    '(': ')',
}

print_brackets = brackets.copy()

while len(brackets) > 0:
    char = brackets.pop(0)
    if OPEN_BRACKETS.search(char.c):
        stack.append(char)
    else:
        color = NC
        if len(stack) > 0 and pairs[stack[len(stack) - 1].c] == char.c:
            stack[len(stack) - 1].color = NC
            char.color = NC
            stack.pop()
        else:
            color = RED

for i in print_brackets:
    print(f"{i.color}{i.c}{NC}", end='')


print()
