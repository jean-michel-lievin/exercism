"""
Your task is to implement a binary search algorithm.
"""
def find(search_list, value):
    """
    param search_list : [int]
    value : int
    return index : int
    """
    left = 0
    right = len(search_list) - 1
    search_list = sorted(search_list)
    while left <= right:
        middle = (left + right) // 2

        if search_list[middle] == value:
            return middle
        if middle < value:
            left = middle + 1
        else:
            right = middle - 1
            
    raise ValueError("value not in array")
