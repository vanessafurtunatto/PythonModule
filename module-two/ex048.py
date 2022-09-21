print('IMC calculator')
weight = float(input('Whats your weight? (KG) '))
height = float(input('Whats your height? (M) '))
imc = weight / (height ** 2)
print('Your IMC is {:.1f}'.format(imc))
if imc < 18.5:
    print('Under weight')
elif 18.5 <= imc < 25:
    print('Ideal weight')
elif 25 <= imc < 30:
    print('Overweight')
elif 30 <= imc < 40:
    print('Obesity')
else:
    print('Morbid obesity')
