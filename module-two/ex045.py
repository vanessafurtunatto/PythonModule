note1 = float(input('Enter the first note: '))
note2 = float(input('Enter the second note: '))
average = (note1 + note2) / 2
print('Between {} and {} the mean is {}'.format(note1, note2, average))
if 7 > average >= 5:
    print('You are in recovery')
elif average < 5:
    print('You are flunked')
elif average >= 7:
    print('You are approved')
