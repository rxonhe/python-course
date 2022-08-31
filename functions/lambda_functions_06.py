def choose_sum_method(method_options, list_to_sum):
    """Choose correct function to use based on dict and length of a list"""
    return method_options[len(list_to_sum)]


if __name__ == "__main__":
    options = {
        2: lambda a, b: a + b,
        3: lambda a, b, c: a + b + c
    }

    list_0 = [1, 2]
    list_1 = [1, 2, 3]

    list_0_sum = choose_sum_method(options, list_0)(*list_0)
    list_1_sum = choose_sum_method(options, list_1)(*list_1)

    print("List 0 sum: {}".format(list_0_sum))
    print("List 1 sum: {}".format(list_1_sum))
