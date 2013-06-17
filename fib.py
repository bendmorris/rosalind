data = raw_input()
n, k = [int(x) for x in data.split()]
def mfib(n, a=1, b=1):
    for _ in range(n-2):
        a, b = b, (a*k)+b
    return b

print mfib(n)
