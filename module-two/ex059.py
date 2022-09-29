from datetime import date
current = date.today().year
major = 0
minor = 0
for people in range(1, 8):
    born = int(input('{} person, what year were you born? '.format(people)))
    age = current - born
    if age >= 21:
        major += 1
    else:
        minor += 1
print('We had {} people of legal age'.format(major))
print('We had {} underage people'.format(minor))


