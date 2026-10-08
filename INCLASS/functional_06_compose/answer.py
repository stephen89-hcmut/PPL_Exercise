from functools import reduce


def compose_recursive(*args):
    if not args:
        return lambda value: value
    if len(args) == 1:
        return args[0]
    rest = compose_recursive(*args[1:])
    return lambda value: rest(args[0](value))


def compose_higher_order(*args):
    return reduce(lambda composed, function: lambda value: function(composed(value)), args, lambda value: value)
