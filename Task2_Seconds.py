seconds = int(input("Введите время в секундах:"))

hours = seconds // 3600
minutes = seconds // 60
minutes = minutes % 60
seconds = seconds % 60
print(f"{hours}:{minutes}:{seconds}")


