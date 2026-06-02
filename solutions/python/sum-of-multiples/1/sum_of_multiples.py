def sum_of_multiples(limit, multiples):

    multiset = [set(range(m, limit, m)) for m in multiples if m > 0]

    return sum(set.union(*multiset)) if multiset else 0

    # return sum({n for m in multiples if m > 0 for n in range(m, limit, m)})