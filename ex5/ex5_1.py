from math import sqrt, floor

x = sqrt(19 - 8 * sqrt(3))
a = floor(x) # x的整数部分
b = x - a

print(a + b + 1 / b)
