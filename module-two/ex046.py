from datetime import date
current = date.today().year
born = int(input('What is your year of birth? '))
age = current - born
print('The athlete is {} years old.'.format(age))
if age <= 9:
    print('Your rating is child')
elif age <= 14:
    print('your rating is childish')
elif age <= 19:
    print('your rating is junior')
elif age <= 25:
    print('your rating is senior')
else:
    print('your rating is master')
