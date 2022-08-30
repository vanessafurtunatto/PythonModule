import random
from math import sqrt, floor

numb = random.randint(1, 10)
root = sqrt(numb)
print('The square root of {} is equal to {}'.format(numb, floor(root)))

