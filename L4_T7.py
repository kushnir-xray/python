from math import factorial
def fact(n):
    for i in range(1, n + 1):
        print(i,  end='= ')
        yield factorial(i)

print("Факториалы чисел:")
for el in fact(7):
    print(el)


