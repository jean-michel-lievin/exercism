"""
Take a nested array of any depth and return a fully flattened array.
"""
def flatten(iterable):
    """
    param iterable: nested array
    return flattened array
    """
    result = []
 
    for item in iterable:
        if isinstance(item, list):
            result.extend(flatten(item))
        elif item is not None:
            result.append(item)

    return result
