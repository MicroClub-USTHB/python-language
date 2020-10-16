print(
    'this program takes an interger input and returns its factorial using recursion\n'
)

var = input("Enter a number: ")

fact = lambda c: 1 if (c == 0 or c == 1) else c * fact(c - 1)
print(fact((int)(var)))