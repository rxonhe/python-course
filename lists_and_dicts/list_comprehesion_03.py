def get_list_0(list_len):
    """return a list with integer numbers"""
    temp_list = []
    for i in range(list_len):
        temp_list.append(i)
    return temp_list


def get_list_1(list_len):
    """return a list with integer numbers using list comprehension"""
    return [i for i in range(list_len)]


def multiply_pairs_by2(x):
    """ Given a list, multiply its pair values by 2"""
    return [value * 2 if value % 2 == 0 else value for value in x]


def remove_pairs(x):
    """ Given a list, remove its pair values"""
    return [value for value in x if value % 2 != 0]


if __name__ == "__main__":
    list_0 = get_list_0(10)
    list_1 = get_list_1(10)

    print(str(list_0))
    print(str(list_1))

    multiplied_pairs = multiply_pairs_by2(list_0)
    print(str(multiplied_pairs))

    removed_pairs = remove_pairs(list_0)
    print(str(removed_pairs))
