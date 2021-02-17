filename = '/Users/flavio/test.txt'

file = open(filename, 'a')

# or

file = open(filename, mode='a')


filename = '/Users/flavio/test.txt'

file = open(filename, 'w')

# or

file = open(filename, mode='w')


filename = '/Users/flavio/test.txt'

file = open(filename, 'w')

file.write('This is a line\n')

file.writelines(['One\n', 'Two'])

file.close()
