from math import hypot
co = float(input('Cathetus opposite: '))
ca = float(input('Cathetus adjacent : '))
hi = hypot(co, ca)
print('The hypotenuse is {:.2f}'.format(hi))
