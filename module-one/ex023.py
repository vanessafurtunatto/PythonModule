from random import choice
n1 = str(input('First student: '))
n2 = str(input('Second student: '))
n3 = str(input('Third student: '))
lis = [n1, n2, n3]
take = choice(lis)
print('The student is: {} '.format(take))
