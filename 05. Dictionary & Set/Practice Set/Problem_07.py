#  If the names of 2 friends are same; what will happen to the program in problem 6? 

favorite_language = {}

name = input("Enter your name: ")
language = input("Enter langauge name: ")
favorite_language.update({name:language})

name = input("Enter your name: ")
language = input("Enter langauge name: ")
favorite_language.update({name:language})

name = input("Enter your name: ")
language = input("Enter langauge name: ")
favorite_language.update({name:language})

name = input("Enter your name: ")
language = input("Enter langauge name: ")
favorite_language.update({name:language})

print(favorite_language)

"""
If two friends have the same name in the program, the previous entry in the dictionary will be overwritten. This is because dictionaries in Python do not allow duplicate keys. Each key must be unique, so if a new value is assigned to an existing key, it will replace the old one.
"""

"""
If the names of two friends are the same but their favorite languages are different, the second friend’s entry will overwrite the first friend’s entry. This happens because dictionary keys must be unique in Python. When the same key is used again, it updates the value for that key, resulting in the loss of the earlier data.
"""