def degree(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result


print(degree(float(input("Введите положительное число:")), int(input("Введите отрицательное число:"))))

