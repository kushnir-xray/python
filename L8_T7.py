class ComplexNumber:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна:')
        return f'z = {self.x + other.x} + {self.y + other.y}'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.x * other.x - (self.y * other.y)} + {self.y * other.x}'

    def __str__(self):
        return f'z = {self.x} + {self.y}'


z_1 = ComplexNumber(1, -2j)
z_2 = ComplexNumber(3j, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
