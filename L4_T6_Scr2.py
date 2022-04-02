from itertools import cycle
list = [4, 1, 2, 9, 2, 9, 1, 6, 8, 9]
c = 0
for el in cycle(list):
    if c > 5:
        break
    print(list)
    c += 1




