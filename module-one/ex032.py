from random import randint
pc = randint(0, 5)
print('Guess what number Im thinking')
person = int(input('whats your guess? '))
if person == pc:
    print('Your win, i think {}'.format(pc))
else:
    print('Your lose, i think {}, no {}!'.format(pc, person))
