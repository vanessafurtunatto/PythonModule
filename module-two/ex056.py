first = int(input('First term: '))
reason = int(input('Reason: '))
ten = first + (10 - 1) * reason
for c in range(first, ten + reason, reason):
    print('{}'.format(c), end=' -> ')
print('Its over.')
