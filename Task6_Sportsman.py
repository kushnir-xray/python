distance = int (input ("Введите пройденный путь в первый день, в км"))
best_result = int(input ("Введите предельное расстояние, в км"))
day = 1
print ("1 -й день", f'{distance:.2f}', "км")

while (distance <= best_result):
    distance = float(distance * 1.1)
    day = day + 1

    print(day, "-й день", f'{distance:.2f}', "км")


