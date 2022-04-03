seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
month = int(input("Введите цифру от 1 до 12:"))
monthes_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
              9: 'Сентябрь', 10: 'Октябрьr', 11: 'Ноябрь', 12: 'Декабрь'}
print(f"Месяц: {monthes_dict[month]}")

if 3 <= month >= 5:
    print(seasons_list[1])
elif  6 <= month >= 7:
    print(seasons_list[2])
elif  9 <= month >= 10:
    print(seasons_list[3])
else :
    print(seasons_list[0])
