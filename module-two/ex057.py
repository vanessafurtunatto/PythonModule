num = int(input('Type a number: '))
t = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m0 The number {} has been divided {} times.'.format(num, t))
if t == 2:
    print('It is')
else:
    print('Is no')
