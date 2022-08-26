def f(x):
    """
    :param x: a number
    :return: 2 + x
    """
    return 2 + x


def add_2_numbers(a, b):
    """
    :param a:
    :param b:
    :return: a+b
    """
    return a + b


def add_n_numbers(*args):
    """
    :param args: n numbers 
    :return: n_0 + n_1 + ... n_n
    """
    total = 0
    for number in args:
        total += number
    return total


def add_n_numbers_v2(*args):
    """
    :param args: n numbers
    :return: n_0 + n_1 + ... n_n
    """
    return sum(args)


if __name__ == '__main__':
    one, two, three, four = 1, 2, 3, 4
    print(f"f(one) = 2 + one = {f(one)}")
    print(f"one + two = {add_2_numbers(one, two)}")
    print(f"one + two + three = {add_n_numbers(one, two, three)}")
    print(f"one + two + three + four = {add_n_numbers_v2(one, two, three, four)}")
