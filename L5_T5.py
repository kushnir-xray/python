from random import randint
with open('spisok.txt', mode='w+', encoding='utf-8') as my_file:
    my_file.write(' '.join([str(randint(1, 1000)) for _ in range(100000)]))
    my_file.seek(0)
    print(sum(map(int, my_file.readline().split())))

