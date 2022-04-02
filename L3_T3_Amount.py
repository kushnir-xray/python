def my_func(num_1, num_2, num_3):
    print(f'Сумма двух наибольших аргументов равна: {num_1 + num_2 + num_3 - min([num_1, num_2, num_3])}')


my_func(int(input('Введите первое число:')),
        int(input('Введите второе число:')),
        int(input('Введите третье число:')))