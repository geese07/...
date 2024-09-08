def print_params(a: object = 1, b: object = 'str', c: object = True) -> object:
    print(a, b, c)
    return a, b, c
print_params()
print_params(b = 25)
values_list = [2.3, False, "str"]
print_params(*values_list)
print_params(c = [1,2,3])
values_list_2 = [54.32, 'str']
print_params(*values_list_2, 42)
values_dict = {'a' : 23, 'b' : "str", 'c' : 12.21}
print_params(**values_dict)
