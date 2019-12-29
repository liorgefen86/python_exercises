# the 'string' data structure is seen in 'data_types' but will be seen
# here again as it is a data structure (depending on the source, a
# string is sometimes considered a data type)

# I will be exploring here in more detail 'strings' and what can be done
# with them.

s = "  This is a StriNg"
print('-' * 15 + 'Slicing' + '-' * 15)
# below are different ways to slice (extract a smaller part) a string
print(s[4])  # [] is the indexing operator used to extract part of data from
# strings, lists, etc.
print(s[-1])  # it is possible to use positive indexes and negative ones
# negative indexes are working from the end of the string
# above example will be extracting the last char of the string
print(s[:])  # ':' is used to extract a sub string. In this case, the
# starting and ending indexes are not provided and there for the entire
# string is extracted
print(s[0:4])  # in this example, the extracted substring is starting
# at index 0 (first char of the string) and end up at index 4 (non-
# inclusive)
print(s[-4:-1])  # the same as above but with negative indexes.
# The substring is starting at the forth most right index and end with
# the last index (-1, non-inclusive)
print(s[:4])  # this example is the same as 'print(s[0:4])'. Omitting an
# index at the beginning or end will be counted as the substring start
# (or end) and the first index (or last index)
print(s[5:])
# the same is valid for negative indexes
print(s[:-3])
print(s[-6:])

print('-' * 15 + 'String Methods and Functions' + '-' * 15)
# length of a string using 'len' function
print(len(s))  # will return the length of the string

# a few additional useful methods
print(s.upper())  # will capitalize the entire string
print(s.lower())  # will put in lower letter entire string
print(s.capitalize())  # will capitalize only the first letter
print(s.title())  # will capitalize every first letter of each word

print(s.find('a'))  # will search for 'a' and return the position
print(s.find('A'))  # will search for 'A' and return the position
# above 2 lines won't return the same result as python is case sensitive
# which means 'a' is different than 'A', therefore, the second line
# will return '-1' to indicate that character wasn't found

print(s.count('i'))  # will return the number of occurrence of a string,
# in this case, 'i' appears 3 times in 's'

print(s.strip())  # strip method is removing leading
# and trailing whitespaces. If a second argument iis given, will remove
# the leading and trailing character, such as below:
print(s.strip('g').upper())
# above use of string methods is showing it is possible to chain several
# methods one after the other. It is possible because python will be
# performing the operation from left to right, therefore, the first
# operation done in this example will be a strip of whitespaces, which
# returns a string, on which the upper method is applied.
print(s.replace('is', 'is not').strip().capitalize())
# the method replace is doing as the name suggest, replacing a substring
# by another string. Here, it will replace 'is' by 'is not'

# looping through strings
# a string is an array of characters and therefore, can be looped
# through using a for or while loop. There are several ways to do so,
# some way are better than other, though.
s = s.strip().capitalize()  # redefining s
print(f'{"-"*50}Looping through string{"-"*50}')
# looping through the different characters of a string
print('Using a for loop and range:', end='\t')
for index in range(len(s)):
    print(s[index], end='')

print('\n' + '-' * 50)

print('Using a while loop:', end='\t')
index = 0
while index < len(s):
    print(s[index], end='')
    index += 1

print('\n' + '-' * 50)

print('Using a for loop:', end='\t')
# the best way though, is to loop through the elements of a string:
for letter in s:
    print(letter, end='')

print('\n')
# using the 'in' operator, as in the for loop, we can create logical
# expression in order to check if a string is in another string
sub_string = 'lunch'
full_string = 'We go for lunch every day at noon'
print('sub_string, %s, is in the string %s: %s' % (sub_string, full_string,
                           sub_string.lower() in full_string.lower()))

# last remark: strings are immutable, which means a string cannot be
# modified. See below example:
# full_string[4] = 'r'
# above statement will throw an error: TypeError: 'str' object does not
# support item assignment.

print(f'\n\n{"-" * 25}Lists data structure{"-" * 25}')

# lists are another data structure in python. It is also called a
# collection. A list can contain any number of elements from different
# types (mixed or not in the same list).
# As a string, a list can be sliced and a sub-list can be extracted.

name_list = ['david', 'maria', 'frank', 'john', 'natalie']
sub_list = name_list[1:3]
print(sub_list)
sub_list = name_list[:3]
print(sub_list)
sub_list = name_list[3:]
print(sub_list)
sub_list = name_list[:]
print(sub_list)

name_list.append('daria')  # add an element to the list at the last position
print(name_list)
name_list.pop()  # remove the last element from the list
print(name_list)
name_list.pop(2) # remove the third element from the list
print(name_list)
name_list.insert(2, 'frank')  # insert an element to the list
print(name_list)
print(name_list.index('frank'))  # return the index of the element
# it will throw an error if the element is not in the list
name_list.sort()  # sort the list
print(name_list)
name_list.reverse()
print(name_list)  # reverse the list
name_list.insert(0, 'frank')
name_list.insert(3, 'frank')
print(name_list.count('frank'))  # return the number of occurrence of the
# element in the list
