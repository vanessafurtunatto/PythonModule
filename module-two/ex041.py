vl = float(input('What is the financing amount? R$: '))
vs = float(input('What is your salary? R$: '))
years = int(input('How many years will you pay? '))
pay = vl / (years * 12)
min = vs * 30 / 100
print('To pay for a house of so many {:.2f}, in {} years, you will have a payment of {:.2f} reais'.format(vl, years, pay))
if pay <= min:
    print('Funding granted!')
else:
    print('Fnding denied!')
