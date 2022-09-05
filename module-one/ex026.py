fname = str(input('Type your full name: ')).strip()
print('Analyzing your name...')
print('In Upper case is {}'.format(fname.upper()))
print('In low case is {}'.format(fname.lower()))
print('This is the size of your name {} letters'.format(len(fname) - fname.count(' ')))
print('Your fist name have {} letters'.format(fname.find(' ')))

