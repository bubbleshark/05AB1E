def vectorized_evaluation(a, b, function, pre_function=None):
    """
    Uses the given function in the form of a lambda and produces a vectorized result if
    at least one of the items is an iterable value. Otherwise, it evaluates it as normal.
    :param a: The first value for the function
    :param b: The second value for the function
    :param function: A 2-arity lambda used for the function
    :param pre_function: A function that is called before vectorization (optional)
    :return: A value or array of values depending on a and b
    """

    if pre_function is not None:
        if type(a) is list:
            a = [pre_function(x) for x in a]
        else:
            a = pre_function(a)

        if type(b) is list:
            b = [pre_function(x) for x in b]
        else:
            b = pre_function(b)

    # When both are lists
    if type(a) is list and type(b) is list:

        # Get the minimum and maximum of both lists in order to prevent index errors
        vector_range = min(len(a), len(b))
        max_range = max(len(a), len(b))
        vectorized_result = []

        # Compute the function for all in range elements
        for index in range(0, vector_range):
            vectorized_result.append(function(a[index], b[index]))

        # Append all out of range elements without being processed
        for index in range(vector_range, max_range):
            if len(a) == max_range:
                vectorized_result.append(a[index])
            else:
                vectorized_result.append(b[index])

        return vectorized_result

    # When only type a is a list
    elif type(a) is list and type(b) is not list:

        vectorized_result = []
        for element in a:
            vectorized_result.append(function(element, b))

        return vectorized_result

    # When only type b is a list
    elif type(a) is not list and type(b) is list:

        vectorized_result = []
        for element in b:
            vectorized_result.append(function(a, element))

        return vectorized_result

    else:
        return function(a, b)


def single_vectorized_evaluation(a, function, pre_function=None):

    if pre_function is not None:
        if type(a) is list:
            a = [pre_function(x) for x in a]
        else:
            a = pre_function(a)

    if type(a) is list:

        vectorized_result = []
        for element in a:
            vectorized_result.append(function(element))

        return vectorized_result

    else:

        return function(a)
