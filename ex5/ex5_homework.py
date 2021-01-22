from math import sqrt

x = sqrt(19 - 8 * sqrt(3))

numerator = (x ** 4) - 6 * (x ** 3) - 2 * (x ** 2) + 18 * x + 23
denominator = x ** 2 - 8 * x + 15

print(numerator / denominator)
