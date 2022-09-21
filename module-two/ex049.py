print('{:=^40}'.format('Van store'))
price = float(input('Shopping price: R$ '))
print(""" What is the payment method?
[1] In cash/check: 10% discount
[2] In cash on card: 5% discount
[3] up to 2x on the card: formal price
[4] 3x or more on the card: 20% interest""")
option = int(input('Which option do you want? '))
if option == 1:
    pay = price - (price * 10 / 100)
    print('Your purchase worth {:.2f} will be for R${:.2f}'.format(price, pay))
elif option == 2:
    pay = price - (price * 5 / 100)
    print('Your purchase worth {:.2f} will be for R${:.2f}'.format(price, pay))
elif option == 3:
    pay = price
    parcel = price / 2
    print('Your purchase worth {:.2f} will be for 2x {:.2f}, total is R${:.2f}'.format(price, parcel, pay))
elif option == 4:
    pay = price + (price * 20 /100)
    tparcel = int(input('How many parcels? ' ))
    parcel = pay / tparcel
    print('Your purchase worth {:.2f} will be for {}x {:.2f}, total is R${:.2f}'.format(price, tparcel, parcel, pay))
else:
    print('Invalid option')
