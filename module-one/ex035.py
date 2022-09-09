distance = float(input('What is the travel distance? '))
if distance <=200:
    price = distance * 0.50
else:
    price = distance * 0.45
print('The price of your trip is R$: {:.2f}'.format(price))
