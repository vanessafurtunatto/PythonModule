sum = 0
count = 0
for c in range(1, 7):
    num = int(input('Type a {} value: '.format(c)))
    if num % 2 == 0:
        sum += 1
        count += 1
print('You entered {} and their sum is {}:'. format(count, sum))
