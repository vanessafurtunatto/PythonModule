num = int( input('Type a number integer: '))
print(''' Choose a base for conversion:
 [ 1 ] For binary 
 [ 2 ] For Octal 
 [ 3 ] For Hexa ''')
options = int(input('Your option: '))
if options == 1:
    print('{} converted to binary is {}'.format(num, bin(num)[2:]))
elif options == 2:
    print('{} converted to octal is {}'.format(num, oct(num)[2:]))
elif options == 3:
    print('{} converted to hexa is {}'.format(num, hex(num)[2:]))
else:
    print('() is option invalid, try again.'. format(num))
