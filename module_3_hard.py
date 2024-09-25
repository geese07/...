def calculate_structure_sum(*args):
    summa = 0
    for each_args in args:
        if isinstance(each_args, int):
            summa += each_args
        elif isinstance(each_args, str):
            summa += len(each_args)
        elif isinstance(each_args, dict):
            summa += calculate_structure_sum(*each_args.keys())
            summa += calculate_structure_sum(*each_args.values())
        elif isinstance(each_args, list) or isinstance(each_args, set) or isinstance(each_args, tuple):
            summa += calculate_structure_sum(*each_args)

    return summa

data_structure = [[1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)