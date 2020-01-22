def left_join(d1, d2):
    """
    Function that a  LEFT JOINs 2 dictionaries into a single data structure.
    All the values in the first dictionary are returned, and if values exist in the “right” dictionary, they are added to the {results dictionary}. If no values exist in the right dictionary, then None should be added to the {results dictionary}
    The key in dictionary case-sensitive, for example "cat" and "Cat" will be treated as a different keys.
    Input: {dictionary1}, {dictionary2}
    Output: {results dictionary}
    """
    results = {}

    for key in d1:
        results[key]=[d1[key]]
        val = None
        if key in d2:
            val = d2[key]
        results[key].append(val)
    return results



