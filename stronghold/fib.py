data = raw_input()
n, k = [int(x) for x in data.split()]
a, b, = 1, 1
for _ in range(n-2):
    a, b = b, (a*k)+b
print b
