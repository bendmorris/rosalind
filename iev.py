import sys

def iev(data):
    '''
    >>> round(iev('1 0 0 1 0 1'), 1)
    3.5
    '''
    xs = [int(x) for x in data.split()]
    ps = [1, 1, 1, 0.75, 0.5, 0]
    return sum([a*b for (a, b) in zip(xs, ps)]) * 2

if sys.stdin.isatty():
    import doctest
    doctest.testmod()
else:
    data = raw_input()
    print iev(data)
