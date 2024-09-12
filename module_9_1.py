# Домашнее задание по теме "Введение в функциональное программирование"

def apply_all_func(int_list, *functions):
    results = {}

    if not isinstance(int_list, list):
        print("Первый аргумент должен быть списком")
        return

    elif not are_all_elements_numbers(int_list):
        print("Некорректные данные, передайте список из чисел")
        return

    for function in functions:
        try:
            result = function(int_list)
            results[function.__name__] = result
        except Exception as exc:
            results[function.__name__] = {"error": f"Ошибка: {exc}"}

    return results


def are_all_elements_numbers(int_list):
    return all(isinstance(element, (int, float)) for element in int_list)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 20, '15', 9], max, min))
print(apply_all_func("not a list", max, min))
