data = raw_input()
letters = sorted(set(data))
print ' '.join([str(data.count(letter)) for letter in letters])