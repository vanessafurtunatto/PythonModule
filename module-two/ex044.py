from datetime import date
current = date.today().year
born = int(input('What is your year of birth? '))
age = current - born
print('Born in {}, are {} years old, in the year of {}'.format(born, age, current))
if age ==18:
    print('you can enlist.')
elif age < 18:
    cal = 18 - age
    print('There are still {} years to enlist'.format(cal))
elif age > 18:
    cal = age -18
    print('You should have enlisted {} years ago'.format(cal))


