import networkx as nx
from typing import Union, List


def create_stairway_graph(stairway: List[int]) -> nx.DiGraph:
    """
    Создает взвешенный направленный граф для платной лестницы.

    :param stairway: список стоимостей ступеней
    :return: взвешенный направленный граф
    """
    graph = nx.DiGraph()
    for i, cost in enumerate(stairway):
        graph.add_node(i)
        if i > 0:
            graph.add_edge(i-1, i, weight=cost)
        if i > 1:
            graph.add_edge(i-2, i, weight=cost)
    return graph


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитывает минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    return nx.shortest_path_length(graph, 0, len(graph)-1, weight='weight')


if __name__ == '__main__':
    stairway = [5, 11, 43, 2, 23, 43, 22, 12, 6, 8]
    stairway_graph = create_stairway_graph(stairway)
    print(stairway_path(stairway_graph))  # 72
