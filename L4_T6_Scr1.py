from itertools import count

print("<<Итератор целых чисел, начиная с указанного>>")
n = int(input("Введите целое число до 15:"))

for el in count(7):
    if el > 15:
        break
    else:
        print(el)

