"""
In the previous file, we could see that the smaller list determines the final list size.
We could add any amount of lists after the first parameter inside the map method.

The zip function does the limiting by the smallest and join them as a tuple (this lesson contains an example)
Then the tuple is unpacked and passed as a parameter to the indicated function.

What is zip good for?
    Iterating through n lists at the same time
    Limiting by the smallest
"""


def custom_map(function, *lists_args):
    """Does the same as built-in map (educational purposes only)"""

    def _execute_for_each(_function, *_args):
        """Call function given the args"""
        return _function(*_args)

    zipped_args = zip(*lists_args)

    get_comments(lists_args)

    return [_execute_for_each(function, *args) for args in zipped_args]


def get_comments(lists_args):
    """Add comments for better understanding of map and zip functions. """
    print("Zipping list args...")
    first_element = list(zip(*lists_args))[0]
    print("First element of zipped args (example): {}".format(first_element))
    # retrieve a list of lists sizes
    sizes_list = list(map(len, lists_args))
    print("Biggest list was len = {}, limited to len = {}".format(max(sizes_list), min(sizes_list)))
    print("Calling function...")


def sum_n_numbers(*numbers):
    return sum(numbers)


if __name__ == '__main__':
    list_0 = list(range(5))
    list_1 = list(range(6))
    list_2 = list(range(7))
    sum_element_wise = custom_map(sum_n_numbers, list_0, list_1, list_2)

    print("""
    List 1: {}
    List 2: {}
    List 3: {}
    Product: {}
    """.format(list_0, list_1, list_2, sum_element_wise))

    sum_element_wise_map = map(sum_n_numbers, list_0, list_1, list_2)
    print("Using built-in map: {}".format(list(sum_element_wise_map)))
