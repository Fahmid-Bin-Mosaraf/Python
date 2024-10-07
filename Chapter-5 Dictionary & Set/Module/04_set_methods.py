my_set = {1, 2, 3, 4, 5, 6}
print(my_set, type(my_set))

my_set.add(7) # Adds an element to the set.
print(my_set)

my_set.update([8,9]) # Adds multiple elements to the set using an iterable.
print(my_set)

my_set.remove(5) # Removes the specified element from the set.Raises a KeyError if the element is not found.
print(my_set)

my_set.discard(4) # Removes the specified element, but does not raise an error if the element is not found.
print(my_set)

elements = my_set.pop() # Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
print(elements)

my_set.clear() # Removes all elements from the set, making it an empty set.
print(my_set)