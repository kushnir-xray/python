class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль невозможно")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(5, 0))
print(DivisionByNull.divide_by_null(5, 2))
print(div.divide_by_null(5.5, 0))