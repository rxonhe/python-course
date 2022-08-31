def get_dict_0(names, values):
    """Given keys and values create and return a dictionary"""
    temp_dict = {}
    for key, value in zip(names, values):
        temp_dict[key] = value
    return temp_dict


def get_dict_1(names, values):
    """Given keys and values create and return a dictionary (Uses Dict Comprehesion)"""
    return {
        key: value for key, value in zip(names, values)
    }


def multiply_pairs_by2(x):
    """ Given a dict, multiply its pair values by 2"""
    return {key: value * 2 if value % 2 == 0 else value for key, value in x.items()}


def remove_pairs(x):
    """ Given a dict, remove its pair values"""
    return {key: value for key, value in x.items() if value % 2 != 0}


if __name__ == "__main__":
    names_0 = ["one", "two", "three", "four"]
    values_0 = [1, 2, 3, 4]

    dict_0 = get_dict_0(names_0, values_0)
    dict_1 = get_dict_1(names_0, values_0)

    print(str(dict_0))
    print(str(dict_1))

    # Multiply Pairs by 2
    multiplied_dict = multiply_pairs_by2(dict_0)

    print(str(multiplied_dict))

    # Remove Pairs
    removed_pairs_dict = remove_pairs(dict_0)

    print(str(removed_pairs_dict))
