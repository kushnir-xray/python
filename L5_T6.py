educate = {}
with open("subjects.txt", encoding="utf-8") as base:
    for s in base:
        hours, statistics = s.split(':')
        hours_sum = sum(map(int, "".join([i for i in statistics if i == ' ' or '9' >= i >= '0']).split()))
        educate[hours] = hours_sum
print(f"print(f'Общее количество часов: , {educate}')")
