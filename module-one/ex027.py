num = int(input('type a number: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analyzing your number {}...'.format(num))
print('Unity is {}'.format(u))
print('Ten is {}'.format(d))
print('Hundred is {}'.format(c))
print('Thousand is {}'.format(m))
