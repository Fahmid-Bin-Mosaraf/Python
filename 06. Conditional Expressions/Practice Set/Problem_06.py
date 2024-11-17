"""Write a program to calculate the grade of a student from his marks from the 
following scheme: 
80 - 100 => A+ 
75 - 80 => A 
70 - 75 => A- 
65 - 70 => B
60 - 65 => C
55 - 60 => D
50 - 55 => E
<50 => F
"""

marks = int(input("Enter your marks: "))

if marks >= 80 and marks <= 100:
    grade = "A+"

elif marks >= 75 and marks < 80:
    grade = "A"

elif marks >= 70 and marks < 75:
    grade = "A-"

elif marks >= 65 and marks < 70:
    grade = "B"

elif marks >= 60 and marks < 65:
    grade = "C"

elif marks >= 55 and marks < 60:
    grade = "D"

elif marks >= 50 and marks < 55:
    grade = "E"

elif marks < 50:
    grade = "F"

print(f"Your Grade is: {grade}")