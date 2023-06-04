#!/usr/bin/python3

print ("Hello, World!");

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

print(days)

if True:
  print ("True")
else:
  print ("False")

word = 'word'

sentence = "This is a sentence."

paragraph = """This is a paragraph. It is
 made up of multiple lines and sentences."""

print(word)
print(sentence)
print(paragraph)

input("\n\nPress the enter key to continue.")

import sys; x = 'Hello Word Python!'; sys.stdout.write(x + '\n')

def add(a, b):
    """Function to add the value of a and b"""
    return a+b

print(add.__doc__)
print(add(3,4))
