def my_virgil(text):
    return text.title()


my_quote = []

for word in input('Введите строку из "Энеиды" П. Вергилия: ').split(' '):
    my_quote.append(my_virgil(word))

print(f'Результат: {" ".join(my_quote)}')
