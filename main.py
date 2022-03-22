# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = float(input('Enter the coefficient of x^2:'))
b = float(input('Enter the coefficient of x:'))
c = float(input('Enter Constant:'))

# Calculate the discriminant
D = (b**2) - (4*a*c)

# Find the Solutions
Sol1 = (-b + cmath.sqrt(D))/2*a
Sol2 = (-b - cmath.sqrt(D))/2*a

print(Sol1,Sol2)
