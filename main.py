# ------------------------------
# Кейс-задача №1
# Дан одномерный массив A размерности N.
# Найти сумму отрицательных элементов,
# расположенных между максимальным и минимальным.
# ------------------------------

def sum_negatives_between_extremes(arr):
    """
    Возвращает словарь с:
    - sum: сумма отрицательных элементов между max и min
    - max_value, max_index: значение и индекс первого максимума
    - min_value, min_index: значение и индекс первого минимума
    - left, right: границы интервала между ними (включительно)
    """
    if len(arr) == 0:
        return {
            "sum": 0,
            "max_value": None,
            "max_index": None,
            "min_value": None,
            "min_index": None,
            "left": None,
            "right": None,
        }

    # Находим индексы первого максимума и первого минимума
    max_value = arr[0]
    min_value = arr[0]
    max_index = 0
    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i

    # Индексы интервала между ними
    left = min(min_index, max_index) + 1
    right = max(min_index, max_index) - 1

    # Если между максимумом и минимумом нет элементов
    if left > right:
        return {
            "sum": 0,
            "max_value": max_value,
            "max_index": max_index,
            "min_value": min_value,
            "min_index": min_index,
            "left": left,
            "right": right,
        }

    # Суммируем только отрицательные
    subsegment = arr[left:right + 1]
    result_sum = sum(x for x in subsegment if x < 0)

    return {
        "sum": result_sum,
        "max_value": max_value,
            "max_index": max_index,
        "min_value": min_value,
        "min_index": min_index,
        "left": left,
        "right": right,
    }


def read_int(prompt):
    """Безопасное чтение одного целого числа."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Ошибка: введите целое число. Попробуйте ещё раз.\n")


def read_int_array(expected_n):
    """Чтение массива из expected_n целых чисел с проверкой."""
    while True:
        line = input(f"Введите {expected_n} целых чисел через пробел: ")
        parts = line.split()

        if len(parts) != expected_n:
            print(
                f"Ошибка: вы ввели {len(parts)} значений, "
                f"а ожидалось {expected_n}. Попробуйте ещё раз.\n"
            )
            continue

        try:
            arr = list(map(int, parts))
            return arr
        except ValueError:
            print("Ошибка: все элементы должны быть целыми числами. Попробуйте ещё раз.\n")


if __name__ == "__main__":
    print("=== Кейс-задача №1: сумма отрицательных элементов между max и min ===\n")

    N = read_int("Введите N (размер массива): ")
    if N <= 0:
        print("Размер массива должен быть положительным. Завершение программы.")
        exit(0)

    A = read_int_array(N)

    info = sum_negatives_between_extremes(A)

    print("\n--- Разбор введённых данных ---")
    print("Массив:", A)
    print(f"Максимальный элемент: {info['max_value']} (индекс {info['max_index']})")
    print(f"Минимальный элемент: {info['min_value']} (индекс {info['min_index']})")

    if info["left"] is None or info["right"] is None or info["left"] > info["right"]:
        print("Между максимумом и минимумом нет элементов.")
        print("\nРезультат: сумма отрицательных элементов между max и min = 0")
    else:
        subsegment = A[info["left"]:info["right"] + 1]
        negatives = [x for x in subsegment if x < 0]

        print(
            f"Элементы между ними (индексы {info['left']}..{info['right']}):",
            subsegment,
        )
        if negatives:
            print("Отрицательные среди них:", negatives)
        else:
            print("Отрицательных элементов между max и min нет.")

        print("\nРезультат: сумма отрицательных элементов между max и min =", info["sum"])

    print("\nПример для понимания:")
    print("Вход:  N = 6, массив = 5 -1 -2 0 -3 1")
    print("Выход: сумма = -3 (так как между 5 и -3 лежат -1 и -2)")
