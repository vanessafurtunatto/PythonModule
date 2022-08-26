print('Salary Calculation')
salary = float(input(' Whats the salary? R$ '))
newSalary = salary + (salary * 15 / 100)
print('For the value {}, with a 15% increase, it will be R$ {}'.format(salary, newSalary))
