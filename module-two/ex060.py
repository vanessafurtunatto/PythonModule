major = 0
minor = 0
for people in range(1, 6):
    weight = float(input('{} person, whats your weight? '.format(people)))
    if people == 1:
        major = people
        minor = people
    else:
        if weight > major:
            major = weight
        if weight < minor:
            minor = weight
print('The biggest weight is {}'.format(major))
print('The minor weight is {}'.format(minor))