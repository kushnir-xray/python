num_1 = int(input ('Введите первое число:'))
num_2 = int(input ('Введите второе число:'))
def numbers_div(num1, num2):
    print(num1 / num2)


if num_2 == 0:
    print ('Деление на ноль невозможно. Введите другое число')
else:
    numbers_div(num_1, num_2)