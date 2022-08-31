def multipy_by2(list_param):
    """Multiply each element of the list by 2"""
    return list(map(lambda x: x * 2, list_param))


def multiply_lists(l_0, l_1):
    """Multiply each element of the first list by the corresponding in the other list"""

    def _could_be_lambda(a, b):
        return a * b

    return list(map(_could_be_lambda, l_0, l_1))


if __name__ == '__main__':
    list_0 = list(range(10))
    print("List with 10 elements, starting at zero : {}".format(list_0))
    list_1 = list(range(1, 11))
    print("List with 10 elements, starting at one : {}".format(list_1))

    multiplied_by_2 = multipy_by2(list_0)
    print("List multiplied by 2 element wise: {}".format(multiplied_by_2))

    multiplied_lists = multiply_lists(list_0, list_1)
    print("""
    First list times the other one, element wise:
    List 1 : {}
    List 2: {}
    Product: {}
    """.format(list_0, list_1, multiplied_lists))

    list_1.append(2)

    different_sized_multiplied_lists = multiply_lists(list_0, list_1)
    print("""
    First list times the other one, element wise:
    List 1 : {}
    List 2: {}
    Product: {}
    Note: The extra element has been ignored
    """.format(list_0, list_1, different_sized_multiplied_lists))
