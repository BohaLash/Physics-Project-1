import math

print('Input values: ')

m = float(input('m [kg] = '))
T = float(input('T [h] = '))
r = float(input('r [m] = '))
g = float(input('g [m/s2] = '))

print('========================')

T *= 60 * 60 # h -> s

R = 2 * math.pi * r * math.sqrt(r/g) / T

print('R = ', R)
