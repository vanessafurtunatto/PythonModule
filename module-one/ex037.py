v1 = int(input('First value: '))
v2 = int(input('Second value: '))
v3 = int(input('Third value: '))
minor = v1
if v2 < v1 and v2 < v3:
    minor = v2
if v3 < v1 and v3 < v2:
    minor = v3
bigger = v1
if v2 > v1 and v2 > v3:
    bigger = v2
if v3 > v1 and v3 > v2:
    bigger = v3
print('The minor value is {}'.format(minor))
print('The bigger value is {}'.format(bigger))

