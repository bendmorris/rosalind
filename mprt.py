import sys
import re
import urllib2

motif = re.compile('N[^P](S|T)[^P]')
url = 'http://www.uniprot.org/uniprot/%s.fasta'

def mprt(data):
    '''
    >>> mprt(['A2Z669', 'B5ZC00', 'P07204_TRBM_HUMAN', 'P20840_SAG1_YEAST'])
    B5ZC00
    85 118 142 306 395
    P07204_TRBM_HUMAN
    47 115 116 382 409
    P20840_SAG1_YEAST
    79 109 135 248 306 348 364 402 485 501 614
    '''
    
    for accession in data:
        accession = accession.strip()
        if not accession: continue
        fasta_file = urllib2.urlopen(url % accession)
        fasta_file.readline()
        sequence = fasta_file.read().replace('\n', '')
        
        matches = motif.finditer(sequence)
        pos = [str(n+1) for n in range(len(sequence)) if motif.match(sequence[n:n+4])]
        if pos:
            print accession
            print ' '.join(pos)
                

if sys.stdin.isatty():
    import doctest
    doctest.testmod()
else:
    data = sys.stdin.read().split('\n')
    mprt(data)
