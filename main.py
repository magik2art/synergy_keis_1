# ------------------------------
# Кейс-задача №1
# Дан одномерный массив A размерности N.
# Найти сумму отрицательных элементов,
# расположенных между максимальным и минимальным.
# ------------------------------

def sum_negatives_between_extremes(arr):
    # Если массив пустой или в нём один элемент → нечего суммировать
    if len(arr) < 2:
        return 0

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

    # Определяем индексы интервала между ними
    left = min(min_index, max_index) + 1
    right = max(min_index, max_index) - 1

    # Если между максимумом и минимумом нет элементов
    if left > right:
        return 0

    # Суммируем только отрицательные
    result = sum(x for x in arr[left:right+1] if x < 0)

    return result


# Пример использования
if __name__ == "__main__":
    N = int(input("Введите N: "))
    A = list(map(int, input("Введите элементы массива через пробел: ").split()))
    print("Сумма отрицательных элементов между max и min:", sum_negatives_between_extremes(A))
    