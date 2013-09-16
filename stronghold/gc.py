import sys
import re
data = sys.stdin.read()
line = re.compile('((?P<id>\>Rosalind_[0-9]{4})(?P<sequence>[^>]+))')
highest = 0
highest_id = None
for _, id, sequence in line.findall(data):
    sequence = sequence.replace('\n', '')
    gc = (sequence.count('G') + sequence.count('C')) / float(len(sequence)) * 100
    if gc > highest:
        highest = gc
        highest_id = id[1:]
print highest_id
print highest