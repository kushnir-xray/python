from functools import reduce

result = [el for el in range(100, 1001, 2)]
print("Список чётных чисел:", list)
print("Произведение всех элементов списка:", reduce(lambda x,y: x*y, result))