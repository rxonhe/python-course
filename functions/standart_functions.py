def f(x):
    """Math function repr"""
    return 2 + x


def add_2_numbers(a, b):
    """Sum of two numbers"""
    return a + b


def add_n_numbers(*args):
    """Sum of n numbers"""
    total = 0
    for number in args:
        total += number
    return total


def add_n_numbers_v2(*args):
    """Sum of n numbers"""
    return sum(args)


if __name__ == '__main__':
    one, two, three, four = 1, 2, 3, 4
    print(f"f(one) = 2 + one = {f(one)}")
    print(f"one + two = {add_2_numbers(one, two)}")
    print(f"one + two + three = {add_n_numbers(one, two, three)}")
    print(f"one + two + three + four = {add_n_numbers_v2(one, two, three, four)}")
