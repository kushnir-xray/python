from sys import argv

script_name, productivity, rate_per_hour, award = argv

print("Имя скрипта: ", script_name)
print("Рассчет заработной платы сотрудника")
print("Выработка в часах: ", productivity)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", award)
print("Заработная плата сотрудника: ", (float(productivity) * float(rate_per_hour)) + float(award))