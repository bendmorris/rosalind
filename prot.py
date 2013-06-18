import sys

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


def prot(data):
    '''
    >>> prot('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')
    'MAMAPRTEINSTRING'
    '''
    result = ''
    while len(data) > 3:
        result += protein_dict[data[:3]]
        data = data[3:]
    
    return result
    

if sys.stdin.isatty():
    import doctest
    doctest.testmod()
else:
    data = raw_input()
    print prot(data)
