# Write a program to accept marks of 6 students and display them in a sorted manner. 

marks = []

s1 = int(input("Enter marks: "))
marks.append(s1)
s2 = int(input("Enter marks: "))
marks.append(s2)
s3 = int(input("Enter marks: "))
marks.append(s3)
s4 = int(input("Enter marks: "))
marks.append(s4)
s5 = int(input("Enter marks: "))
marks.append(s5)
s6 = int(input("Enter marks: "))
marks.append(s6)
s7 = int(input("Enter marks: "))
marks.append(s7)

marks.sort()
print(marks)