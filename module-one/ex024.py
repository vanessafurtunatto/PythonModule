from random import shuffle
n1 = str(input('First student: '))
n2 = str(input('Second student: '))
n3 = str(input('Third student: '))
lis = [n1, n2, n3]
shuffle(lis)
print('The order of presentation will be:' )
print(lis)
