"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    # Проверяем, что массив не пуст
    if len(arr) == 0:
        print("Массив пуст")
        return None

    current_min = arr[0]
    for value in arr:

        if value < current_min:
            current_min = value

    return current_min


arr = [-4, 2, 9, 6, 5, -1, 4, 2, -9, 6, 5, 1, 0]
print(min_search(arr))
