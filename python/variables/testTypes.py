#!/usr/bin/python3

'''
Numeric - int, float, complex
'''

var1 = 1
var2 = 10
var3 = 10.023

print(var1)
print(var2)
print(var3)

a = 100
print("The type of variable having value", a, " is ", type(a))

b = 20.345
print("The type of variable having value", b, " is ", type(b))

c = 10+3j
print("The type of variable having value", c, " is ", type(c))

input('press any key to continue')
print()

'''
String - str
'''

str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string
print (str[2:5])     # Prints characters starting from 3rd to 5th
print (str[2:])      # Prints string starting from 3rd character
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

input('press any key to continue')
print()

'''
Sequence - list, tuple, range
'''

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists
print()

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples
print()

for i in range(5):
  print(i)

for i in range(1, 5):
  print(i)

for i in range(1, 5, 2):
  print(i)

input('press any key to continue')
print()

'''
Binary - bytes, bytearray, memoryview
'''

'''
Mapping - dict
'''

dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

input('press any key to continue')
print()

'''
Boolean - bool
'''

a = True
# display the value of a
print(a)

# display the data type of a
print(type(a))

a = 2
b = 4
print(bool(a==b))
print(a==b)
a = None
print(bool(a))
a = ()
print(bool(a))
a = 0.0
print(bool(a))
a = 10
print(bool(a))

input('press any key to continue')
print()

'''
Set - set, frozenset
'''
