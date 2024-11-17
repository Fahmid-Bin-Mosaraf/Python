# Write a program which finds out whether a given name is present in a list or not. 

list = ["Fahmid", "Famel", "Sojib", "Junaed", "Elmi"]

name = input("Enter your name: ")

if(name in list):
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")