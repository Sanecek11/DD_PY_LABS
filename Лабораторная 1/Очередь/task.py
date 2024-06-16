"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало очереди находится в начале списка, конец - в конце.
        """
        self.queue_list = []

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        Сложность: O(1)
        """
        self.queue_list.append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        Сложность: O(n), так как в Python списки удаляются элементы с конца.
        """
        if not self.is_empty():
            return self.queue_list.pop(0)
        else:
            raise IndexError("Очередь пуста")

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        Сложность: O(n), где n - количество элементов до индекса.
        """
        try:
            return self.queue_list[ind]
        except IndexError:
            raise IndexError("Индекс вне границ очереди")

    def clear(self) -> None:
        """
        Очистка очереди.
        Сложность: O(n), где n - количество элементов в очереди.
        """
        self.queue_list.clear()

    def __len__(self):
        """ Количество элементов в очереди.
        Сложность: O(1).
        """
        return len(self.queue_list)

    def is_empty(self) -> bool:
        """
        Проверка, является ли очередь пустой.
        Сложность: O(1).
        """
        return len(self.queue_list) == 0
