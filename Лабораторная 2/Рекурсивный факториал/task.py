def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


k = 7
print(factorial_recursive(k))
