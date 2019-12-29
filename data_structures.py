# the 'string' data structure is seen in 'data_types' but will be seen
# here again as it is a data structure (depending on the source, a
# string is sometimes considered a data type)

# I will be exploring here in more detail 'strings' and what can be done
# with them.

s = "  This is a StriNg"

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

print(s.count('i'))  # will return the number of occurence of a string,
# in this case, 'i' appears 3 times in 's'

print(s.strip())  # strip method is removing leading
# and trailing whitespaces. If a second argument iis given, will remove
# the leading and trailing character, such as below:
print(s.strip('g').upper())
