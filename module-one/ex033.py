speed = float(input('Current speed'))
if speed > 80:
    print('You have been fined, the limit is 80 km')
    m = (speed-80) * 7
    print('You will pay R${:.2f}!'.format(m))
else:
    print('Everithing ok! good day!')