data = raw_input()
data = data[::-1]
for (x, y) in [('G', 'C'), ('T', 'A')]:
    data = data.replace(x, '?')
    data = data.replace(y, x)
    data = data.replace('?', y)
print data