import sys
import math

def prob(data):
    '''
    >>> prob("""ACGATACAA
    ... 0.129 0.287 0.423 0.476 0.641 0.742 0.783""")
    -5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009
    '''
    sequence, a = data.strip().split('\n')
    a = [float(x) for x in a.split()]
    for n in a:
        p = reduce(lambda x, y: x*y, 
                   [n/2 if x in 'GC' else (1-n)/2 for x in sequence])
        print round(math.log(p, 10), 3),

if sys.stdin.isatty():
    import doctest
    doctest.testmod()
else:
    data = sys.stdin.read()
    prob(data)
