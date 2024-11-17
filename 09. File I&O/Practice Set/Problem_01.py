# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’. 

file = open("poems.txt")

content = file.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")
else:
    print("The word twinkle is not present in the content")

file.close()
