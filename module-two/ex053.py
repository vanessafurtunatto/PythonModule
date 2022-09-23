add = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        add += c
        cont += 1
print('The sum of the {} requested values is {}'.format(cont, add))
