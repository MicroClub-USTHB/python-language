import re
from collections import deque
# operands, operators = [], []

print('Reverse Polish Notation\n')

expression = input("Enter a mathematical expression :\n").split()
print(expression)
# operands = [re.findall(r'\d+', expression)]
# operators = [re.findall(r'\D+', expression)]

#function to evalute the first operation
def evaluate(liste):
    var = deque(liste)
    result = 0

    op1 = int(var.popleft())

    op2 = int(var.popleft())
    operation = var.popleft()
    if (operation == '*'):
        result = op1 * op2
    if (operation == '+'):
        result = op1 + op2
    if (operation == '-'):
        result = op1 - op2
    if (operation == '/'):
        result = op1 / op2
    var.appendleft(str(result))
    return list(var)


while (len(expression) > 1):
    expression = evaluate(expression)
print(expression[0])


