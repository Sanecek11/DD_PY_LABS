from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    pt = [[0] * m for _ in range(n)]
    pt[0][0] = 1  # левый верхний угол

    for i in range(n):
        for j in range(m):
            if i > 0:
                pt[i][j] += pt[i-1][j]  # добавляем пути сверху
            if j > 0:
                pt[i][j] += pt[i][j-1]  # добавляем пути слева
            if i > 0 and j > 0:
                pt[i][j] += pt[i-1][j-1]  # добавляем диагональные пути
    return pt


if __name__ == '__main__':
    paths = car_paths(4, 2)
    print(paths[-1][-1])  # 7
