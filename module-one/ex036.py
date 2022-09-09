from datetime import date
year = int(input('What year do you want to review? '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Year {} is leap Year'.format(year))
else:
    print('Year {} is not a leap year'.format(year))
