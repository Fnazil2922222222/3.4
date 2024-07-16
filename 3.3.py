def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)
print(print_params(c=[1,2,3]))

values_list = [5, 6, 7]
values_dict = {"a": 2, "b": 3, "c": 4}
print_params(**values_dict)
print(*values_list)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)