tuple = (1, 2, 4, "Famel", True)
print(tuple)

print(type(tuple)) # type

print(len(tuple)) # tuple length

number = (1,) # tuple with one item
print(type(number))

name = ("Fahmid", "Famel", "Sojib", "Rabi", "Sanjit")
print(name[1]) # access tuple items
print(name[-1]) # negative indexing
print(name[2:5]) # range of indexes

if "Fahmid" in name: # check if items exists
    print("Yes")