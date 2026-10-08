from functools import reduce


def flatten_lst_comp(lst):
    return [element for group in lst for element in group]


def flatten_recursive(lst):
    if not lst:
        return []
    return list(lst[0]) + flatten_recursive(lst[1:])


def flatten_higher_order(lst):
    return reduce(lambda result, group: result + list(group), lst, [])
