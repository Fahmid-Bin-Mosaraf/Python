# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

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

""" Another method
favorite_languages = {}

for _ in range(4):
    name = input("Enter your name: ")
    language = input(f"Hi {name}, what's your favorite language: ")
    favorite_languages[name] = language

print(favorite_languages)

"""