#  Write a program to input name, marks and phone number of a student and format it using the format function like below: “The name of the student is Fahmid, his marks are 72 and phone number is 99999888” 


name = input("Enter the name of the student: ")
marks = input("Enter the marks of the student: ")
phone = input("Enter the phone number of the student: ")

student = "The name of the student is {}, his marks are {} and phone number is {}."

print(student.format(name, marks, phone))