import sys
r = sys.stdin.read().lower()
print '%s %s %s %s' % tuple([r.count(x) for x in 'acgt'])