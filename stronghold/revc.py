def revc(data):
    data = data[::-1]
    for (x, y) in [('G', 'C'), ('T', 'A')]:
        data = data.replace(x, '?')
        data = data.replace(y, x)
        data = data.replace('?', y)
    return data

if __name__ == '__main__':
    data = raw_input()
    print revc(data)