""" Can you change the values inside a list which is contained in set S? 
s = {8, 7, 12, "Fahmid", [1,2]}
"""

s = {8, 7, 12, "Fahmid", [1, 2]}

"""
No, i cannot have a list as an element inside a set in Python because sets only allow immutable (hashable) data types as their elements. Lists are mutable and, therefore, cannot be included in a set. Attempting to include a list in a set will result in a TypeError.
"""