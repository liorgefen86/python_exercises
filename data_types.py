# python is a strongly and dynamically typed language, which means:
# dynamically typed:
#   a variable, or container, does not need to be declared with a type,
#   it will be inferred at runtime. Also, a variable can contain any
#   data type, even if it was previously used for another type.
#   Below code will run in Python but won't be working in a static
#   typed language, such a C#.

var1 = "this is a string"
print(type(var1))
var1 = 34
print(type(var1))

# strongly typed:
#   it is not possible to do operation between incompatible types, such
#   as integer and string. Below code won't be working in python because
#   the data type are not compatible:

# print('1' + 1) # or
# print(1 + '1')

#   But if we change the data type before doing an operation, the code
#   will run:

print(str(1) + '1')
print(int('1') + 1)

# compatible types are such as integer and floats, strings and chars
a = 1
b = 1.0
print(f"the type of 'a' is {type(a)} and the type of 'b' is {type(b)}")
print(a + b)

# some 'operations' can be done on strings and integers, such as '*',
# which will duplicate the string a certain number of time, indicated by
# the integer
print("this is a string" * 3)
print(3 * "this is a string")

# note that is works only with integers. If multiplied by a float, a
# TypeError will be thrown

# python has the possibility to work with complex numbers
com = complex(3, 5)  # a complex number is created by calling the
# complex function. The first argument is the real part and the second
# the imaginary part. We can extract each part from the number by using
# real and imag methods
print(com.real)
print(com.imag)

# the last data type in python is the boolean. A boolean can be defined
# using True or False. But is can also be defined using a logical
# statement, which will be evaluated to True or False
b1 = True
b2 = False
b3 = 3 > 4  # that's a logical statement which will return False,
# because 3 is not greater than 4
print(f'b1: {b1},\nb2: {b2},\nb3: {b3}')