"""
Write a program to greet all the person names stored in a list ‘l’ and which starts with F. 
l = ["Fahmid", "Omi", "Junaed", "Famel"]
"""

l = ["Fahmid", "Omi", "Junaed", "Famel"]
for name in l:
    if(name.startswith("F")):
        print(f"Hello {name}")

