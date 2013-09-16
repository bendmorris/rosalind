import sys

def subs(data):
    '''
    >>> subs('GATATATGCATATACTT\\nATAT')
    '2 4 10'
    '''
    x, y = data.split('\n')
    return ' '.join([str(n+1) for n in range(len(x)) if x[n:].startswith(y)])
    

if sys.stdin.isatty():
    import doctest
    doctest.testmod()
else:
    data = sys.stdin.read().strip()
    print subs(data)
