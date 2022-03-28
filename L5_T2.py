with open("PEP.txt") as read_file:
    all_lines = read_file.readlines()
for num, line in enumerate(all_lines):
    print(f"В строке {num + 1}: {len(line.split())} слов(а)")
print(f"Количество строк: {len(all_lines)}")