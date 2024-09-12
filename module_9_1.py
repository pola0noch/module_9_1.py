# Домашнее задание по теме "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    results = {}

    if not isinstance(int_list, list):
        return "Первый аргумент должен быть списком"

    if not are_all_elements_numbers(int_list):
        return "Некорректные данные, передайте список из чисел"

    for function in functions:
        result = function(int_list)
        results[function.__name__] = result

    return results

def are_all_elements_numbers(int_list):
    return all(isinstance(element, (int, float)) for element in int_list)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 20, '15', 9], max, min))
print(apply_all_func("not a list", max, min))
