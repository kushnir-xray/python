with open("w_salary.txt") as read_file:
    f_average_salary = 0
    lines = read_file.readlines()
    for line in lines:
        s_name, salary = line.split()
        salary = float(salary)
        f_average_salary += salary
        if salary < 20000:
            print(f"\t{s_name} {salary}")
    if len(lines) > 0:
        f_average_salary /= len(lines)
        print(f"Средняя зарплата: {f_average_salary:.2f}")