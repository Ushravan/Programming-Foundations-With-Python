#Get Grades
#Write a program to calculate the grade of the student based on marks he/she scored.
#Input

#The first line of input will contain a float.
#Output

#If the given marks are greater than 85, print "A".
#If the given marks are greater than 70 and less than or equal to 85, print "B".
#If the given marks are greater than or equal to 60 and less than or equal to 70, print "C".
#If the given marks are less than 60, print "F".
#Explanation

#For example, if the given marks of a student are 70.5, your code should print the grade "B".
#Similarly, if the marks of a student are 90, your code should print the grade "A".

Marks = float(input())

if Marks> 85:
    print("A")
elif  Marks >70:
    print("B")
elif Marks >= 60:
    print("C")
else:
    print("F")
