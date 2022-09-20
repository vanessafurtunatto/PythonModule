name = str(input('Whats your name? '))
if name == 'Vanessa':
    print('Beautiful name!')
elif name == 'Rhuan' or name == 'Felipe':
    print('Awesome name!')
else:
    print('Your name is normal.')
print('Have a nice day, {}. '.format(name))
