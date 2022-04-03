class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'Размер клетки равен: {self.quantity + other.quantity} ячейкам'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f'Размер клетки равен: {sub} ячейкам'

    def __truediv__(self, other):
        return f'Размер клетки равен: {self.quantity // other.quantity} ячейкам'

    def __mul__(self, other):
        return f'Размер клетки равен: {self.quantity * other.quantity} ячейкам'




cell = Cell(36)
cell_2 = Cell(3)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
