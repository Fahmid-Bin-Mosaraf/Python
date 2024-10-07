#  Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

words = {
    "valo" : "good",
    "kharap": "bad",
    "biral": "cat",
    "kukur": "dog",
    "mach": "fish"
}

word = input("Enter the word you want meaning of: ")

print(words[word])