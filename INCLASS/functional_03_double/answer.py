def double_lst_comp(lst):
    return [value * 2 for value in lst]


def double_recursive(lst):
    if not lst:
        return []
    return [lst[0] * 2] + double_recursive(lst[1:])


def double_higher_order(lst):
    return list(map(lambda value: value * 2, lst))
