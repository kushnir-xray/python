my_list = list(input("Введите любое целое число:"))

if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        el = my_list [i]
        my_list[i] = my_list[i+1]
        my_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)