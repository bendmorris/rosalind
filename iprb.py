import sys

def iprb(data):
    '''
    k dominant
    m heterozygous
    n recessive
    
    Individual A    AA                      Aa                      aa
                    k/t                     0.5*m/t                 0*n/t
    Individual B    AA      Aa      aa      AA      Aa      aa      AA      Aa      aa
                    k-1/t-1 m/t-1   n/t-1   k/t-1   m-1/t-1 n/t-1   k/t-1   m/t-1   n-1/t-1
    
    >>> round(iprb('2 2 2'), 5)
    0.78333
    >>> iprb('1 0 1')
    1.0
    >>> iprb('1 1 0')
    1.0
    >>> iprb('0 1 1')
    0.5
    >>> iprb('2 1 0')
    1.0
    >>> iprb('5 0 0')
    1.0
    >>> iprb('5 1 0')
    1.0

    '''
    k, m, n = [int(x) for x in data.split()]
    population = [(1., k), (0.5, m), (0., n)]
    combinations = [(a, b) for a in population for b in population]
    t = (k + m + n)
    return sum([(x + y - (x*y)) * (a * (b if x!=y else b-1))/(t*(t-1)) for (x,a), (y,b) in combinations])

if sys.stdin.isatty():
    import doctest
    doctest.testmod()
else:
    data = raw_input()
    print iprb(data)
