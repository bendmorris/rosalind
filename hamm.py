import sys

def hamm(data):
    '''
    >>> hamm('GAGCCTACTAACGGGAT\\nCATCGTAATGACGGCCT')
    7
    '''
    x, y = data.strip().split('\n')
    return len([1 for n in range(len(x)) if x[n] != y[n]])

if sys.stdin.isatty():
    import doctest
    doctest.testmod()
else:
    data = sys.stdin.read()
    print hamm(data)
