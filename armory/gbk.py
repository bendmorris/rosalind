import sys
from Bio import Entrez

r = sys.stdin
genus = r.readline().strip()
d1 = r.readline().strip()
d2 = r.readline().strip()

Entrez.email = 'ben@bendmorris.com'
search_term = '("%s"[Organism] AND ("%s"[PDAT] : "%s"[PDAT]))' % (genus, d1, d2)
search = Entrez.esearch(db='nucleotide', term=search_term)
record = Entrez.read(search)

print record['Count']
