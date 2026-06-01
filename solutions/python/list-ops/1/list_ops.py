"""
Implement a series of basic list operations, 
without using existing functions.
"""
def append(list1, list2):
    """
    Given two lists, add all items in the second list to the end of the first list
    """
    return list1 + list2


def concat(lists):
    """
    Given a series of lists, combine all items in all lists into one flattened list
    """
    return [l for list in lists for l in list]


def filter(function, list):
    """
    Given a predicate and a list, return the list of all items for which predicate(item) is True
    """
    return [item for item in list if function(item)]


def length(list):
    """
    Given a list, return the total number of items within it
    """
    return len(list)


def map(function, list):
    """
    Given a function and a list, return the list of the results of applying function(item) on all items
    """
    return [function(item) for item in list]


def foldl(function, list, initial):
    """
    Given a function, a list, and initial accumulator, 
    fold (reduce) each item into the accumulator from the left
    """
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator
    

def foldr(function, list, initial):
    """
    Given a function, a list, and an initial accumulator, 
    fold (reduce) each item into the accumulator from the right)
    """
    accumulator = initial
    for item in list[::-1]:
        accumulator = function(accumulator, item)
    return accumulator

def reverse(list):
    """
    Given a list, return a list with all the original items, but in reversed order
    """
    return list[::-1]
