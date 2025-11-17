x = 1 #int
y = 2.9 #float
z = 1j #complex

# To verify the type of any object in Python, use the "type()" function"

# All below are integer
# int/integer, is a whole number, positive or negative, without decimals, of unlimited length
x = 1
y = 3564789201863272911819
z = -2

# All below are Float
# float/floating point number is a number, positive or negative, containing one or more decimals
x = 1.10
y = 1.0
z = -45.444
# Float can also be scientific numbers with an "e/E" to indicate the power of 10
x = 35e10
print(type(x))

# All below are Complex Number
# Complex number are written with a "j" as the imaginary par
x = 3+5j
y = 5j
z = -5j

# Type Conversion
# You can convert from one type to another with the int(), float( and complex (), methods)
x = 1
y = 6.9
z = 1
# Proses peng-convertan
x = (float(x))
y = (int(y))
z = (complex(z))
print(x)
print(y)
print(z)

# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers. Import the random module, and display a random number from 1 to 9:
import random
print(random.randrange(1, 20))