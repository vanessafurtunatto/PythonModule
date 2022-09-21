from random import randint
from time import sleep
items = ('Rock', 'Paper', 'Scissors')
computer = randint(0, 2)
print("""Your options: 
[0] Rock
[1] Paper
[2] Scissors""")
play = int(input('Whats your move? '))

print('Are')
sleep(1)
print('You')
sleep(1)
print('Ready?')
sleep(1)

print('-=' * 10)
print('The computer chose {}'.format(items[computer]))
print('The play chose {}'.format(items[play]))
print('-=' * 10)

if computer == 0:
    if play == 0:
        print('All right, well call it a draw.')
    elif play == 1:
        print('Play win')
    elif play == 2:
        print('Computer win')
    else:
        print('Invalid move.')

elif computer == 1:
    if play == 0:
        print('Computer win')
    elif play == 1:
        print('All right, well call it a draw.')
    elif play == 2:
        print('Play win')
    else:
        print('Invalid move.')

elif computer == 2:
    if play == 0:
        print('Play win')
    elif play == 1:
        print('Computer win')
    elif play == 2:
        print('All right, well call it a draw.')
    else:
        print('Invalid move.')
