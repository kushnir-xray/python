my_list = [13, 2.3, (7 + 8j), [12, 13], "Питон", [tuple('Python')], {'mutable': 'list', 'immutable': 'tuple'}, (13, 14), range(13), None, -30, 'True', True, 9.5]

def my_type(element):
    for element in range(len(my_list)):
        print(type(my_list[element]))
    return
my_type(my_list)