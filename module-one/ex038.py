salary = float(input('Whats you salary? R$: '))
if salary <= 1250:
    ns = salary + (salary * 15 / 100)
else:
    ns = salary + (salary * 10 / 100)
print('If your salary was {:.2f}, it will be {:.2f}'.format(salary, ns))
