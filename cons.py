import sys
import collections

def cons(data):
    '''
    >>> cons(""">Rosalind_1
    ... ATCCAGCT
    ... >Rosalind_2
    ... GGGCAACT
    ... >Rosalind_3
    ... ATGGATCT
    ... >Rosalind_4
    ... AAGCAACC
    ... >Rosalind_5
    ... TTGGAACT
    ... >Rosalind_6
    ... ATGCCATT
    ... >Rosalind_7
    ... ATGGCACT""")
    ATGCAACT
    A: 5 1 0 0 5 5 0 0
    C: 0 0 1 4 2 0 6 1
    G: 1 1 6 3 0 1 0 0
    T: 1 5 0 0 0 1 1 6
    '''
    sequences = []
    sequence = None
    for line in data.split('\n'):
        line = line.strip()
        if not line: continue
        if line.startswith('>'):
            if sequence: sequences.append(sequence)
            sequence = ''
        else:
            sequence += line
    if sequence: sequences.append(sequence)

    letters = 'ACGT'
    results = {x: [] for x in letters}
    consensus = ''
    for n in xrange(len(sequences[0])):
        counter = collections.Counter([sequence[n] for sequence in sequences])
        for letter in letters:
            results[letter].append(counter[letter])
        consensus += counter.most_common()[0][0]
    print consensus
    for letter in letters:
        print ('%s: ' % letter) + ' '.join([str(x) for x in results[letter]])

if sys.stdin.isatty():
    import doctest
    doctest.testmod()
else:
    data = sys.stdin.read()
    print cons(data)
