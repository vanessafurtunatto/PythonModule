print('Discount Calculator')
price = float(input('How much price? R$ '))
newprice = price - (price * 5 / 100)
print('For the value {:.2f}, with a 5% discount, it will be R$ {:.2f}'.format(price,newprice))
