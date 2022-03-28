f_1 = open("enter.txt", 'w')
while True:
    a = input('Введите новую строку или нажмите "Enter": ')
    if not a:
        break
        print(a, file=f_1)
f_1.close()