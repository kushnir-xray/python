with open("C:\Users\kushn\Desktop\GeekBrains\Python\numbers.txt") as my_file, \
        open("C:\Users\kushn\Desktop\GeekBrains\Python\numbers.txt", "w", encoding="utf-8") as new_file:
    number_list = ["Один", "Два", "Три", "Четыре", "Пять", "Шесть", "Семь"]
    lines = my_file.readlines()
    for num, line in enumerate(lines):
        if len(line):
            words = line.split()
            print(f"{number_list[num]} {words[1]} {words[2]}", file=new_file)
