import sys

def fibd(data):
    '''
    >>> fibd('6 3')
    4
    >>> fibd('1 3')
    1
    >>> fibd('2 3')
    1
    >>> fibd('3 3')
    2
    >>> fibd('4 3')
    2
    >>> fibd('5 3')
    3
    >>> fibd('6 3')
    4
    '''
    n, m = [int(x) for x in data.split()]
    x = [1, 1]
    if n <= len(x): return x[n-1]
    for _ in range(n-len(x)):
        x.append(x[-1] + x[-2])
        if len(x) > m:
            dead = x.pop(0)
            x = map(lambda y: y-dead, x)
    return x[-1]

if sys.stdin.isatty():
    import doctest
    doctest.testmod()
else:
    data = raw_input()
    print fibd(data)
