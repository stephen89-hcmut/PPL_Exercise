def lessThan_lst_comp(n, lst):
    return [value for value in lst if value < n]


def lessThan_recursive(n, lst):
    if not lst:
        return []
    first = [lst[0]] if lst[0] < n else []
    return first + lessThan_recursive(n, lst[1:])


def lessThan_higher_order(n, lst):
    return list(filter(lambda value: value < n, lst))
