# Write a python function to remove a given word from a list ad strip it at the same time. 

def remove(list, word):
    n = []
    for i in list:
        if not(i == word):
            n.append(i.strip(word))
    return n

list = ["Fahmid", "Famel", "Famel", "Sojib", "Rabi", "Sabab"]

print(remove(list, "el"))