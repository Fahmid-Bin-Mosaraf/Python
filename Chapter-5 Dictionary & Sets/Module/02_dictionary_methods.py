marks = {
    "Fahmid": 100,
    "Famel": 200,
    "Sojib": 300
}

print(marks.items()) # Returns a list containing a tuple for each key value pair

print(marks.keys()) # Returns a list containing the dictionary's keys

print(marks.values()) # Returns a list of all the values in the dictionary

marks.update({"Famel": 180}) # Updates the dictionary with the specified key-value pairs
print(marks)

print(marks.get("Famel")) # Returns the value of the specified key

new_dict = marks.copy() # Returns a copy of the dictionary
print(new_dict)

new_dict.clear() # Removes all the elements from the dictionary
print(new_dict)