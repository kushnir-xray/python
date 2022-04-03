def calculate_sum(*numbers):
    sum = 0
    mark = False
    for num in numbers:
        try:
            if num:
                sum += float(num)
        except ValueError:
            mark = True
    return sum, mark

general_sum = 0

while True:
    numbers = input('Введите числа через пробел: ').split(' ')
    sum, mark = calculate_sum(*numbers)
    general_sum += sum
    print(f'сумма {general_sum}')

    if mark:
        break