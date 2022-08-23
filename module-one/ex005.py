print('Information about arithmetic operators')
any1 = int(input('Type a value: '))
any2 = int(input('Type other value: '))
s = any1 + any2
m = any1 * any2
d = any1 / any2
di = any1 // any2
e = any1 ** any2
print('The sum is {}, the product is {} and division is {:.2f}'.format(s, m, d), end=' ')
print('the entire division is {} and the power {}'.format(di, e))

