def list_example_0():
    """
    Creates a list of numbers and iterate over it printing them.
    """
    numbers_0 = [1, 2, 3, 4]
    for number in numbers_0:
        print(number)


def dict_example_0():
    """
    Creates a dictionary of numbers and print it's keys.
    """

    numbers_dict_0 = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4
    }
    print("Keys of numbers dict {}".format(str(numbers_dict_0.keys())))


def dict_example_1():
    """
    Creates a dictionary of numbers and iterate over it printing them.
    """

    numbers_dict_0 = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4
    }

    for key, value in numbers_dict_0.items():
        print("{}: {}".format(key, value))


if __name__ == '__main__':
    list_example_0()
    dict_example_0()
    dict_example_1()
