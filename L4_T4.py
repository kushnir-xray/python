source_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
required_list = [el for el in source_list if source_list.count(el) == 1]

print("Исходный список:\l", source_list)
print("Элементы списка, не имеющие повторений:\l", required_list)