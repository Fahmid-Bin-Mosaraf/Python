# Write a program to find out whether a given post is talking about “Fahmid” or not.

post = input("Enter the post: ")

if("Fahmid".lower() in post.lower()):
    print("This post is talking about Fahmid")
else:
    print("This post is not talking about Fahmid")