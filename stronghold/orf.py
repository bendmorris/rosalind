import sys
from revc import revc

proteins = '''UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G'''.split()

pairs = []
while proteins:
    pairs.append((proteins.pop(0), proteins.pop(0)))
protein_dict = dict(pairs)


def orf(data):
    '''
    >>> orf('>Rosalind_99\\nAGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG')
    MLLGSFRLIPKETLIQVAGSSPCNLS
    M
    MGMTPRLGLESLLE
    MTPRLGLESLLE
    '''

    data = ''.join(data.split('\n')[1:])
    rev_comp = revc(data)
    proteins = set()
    for sequence in (data, data[1:], data[2:], rev_comp, rev_comp[1:], rev_comp[2:]):
        sequence = sequence.replace('T', 'U')
        n = 0
        started = False
        while n < len(sequence):
            if sequence[n:n+3] == 'AUG':
                started = True

            if started:
                a = 0
                p = 'M'
                while True:
                    n += 3
                    a += 3
                    try:
                        protein = protein_dict[sequence[n:n+3]]
                        if protein == 'Stop':
                            if not p in proteins: print p
                            proteins.add(p)
                            break
                        else: p += protein
                    except KeyError:
                        break
                n -= a
                started = False
            n += 3

if sys.stdin.isatty():
    import doctest
    doctest.testmod()
else:
    data = sys.stdin.read()
    orf(data)
