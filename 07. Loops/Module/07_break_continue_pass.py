# break statement
list = ["Fahmid", "Famel", "Omi"]
for i in list:
    print(i)
    if i == "Famel":
        break


# continue statement
list = [100, 200, 300, 400, 500]
for i in list:
    print(i)
    if i == 400:
        continue


# pass statement
list = [1, 2, 3, 4, 5]
for i in list:
    pass
# without pass, the program will throw an error