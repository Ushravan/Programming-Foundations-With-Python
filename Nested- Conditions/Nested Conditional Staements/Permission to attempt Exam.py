#Permission to attempt Exam
#Given a student's percentage of attendance and status of having a medical report. Write a program to decide if a student is eligible to take the final exam.
#Input

#The first line of input will contain a string.
#The second line of input will contain a character(either "Y" or "N").
#Output

#If the student has greater than or equal to 75% of attendance, print "Allowed to write exam".
#If the student has less than 75% of attendance and has a medical reason is equal to "Y", print "Allowed to write exam".
#If the student has attendance less than 75% with no medical reason is equal to "N", print "Cannot write exam".
#Explanation

#For example, if the given student has an attendance of 80%, which is greater than the required percentage, the output should be "Allowed to write exam".
#Similarly, if the given student has an attendance of 70% and the medical reason "Y". As the student has the medical reason, the output should be "Allowed to write exam".
#Whereas, if the given student has an attendance of 72%, which is less than the required percentage and the medical reason "N". As the student has no medical reason, the output should be "Cannot write exam".


A = input()
B = input()
length = len(A)
A= A[:length-1]
A=int(A)
if A>75:
    print("Allowed to write exam")
elif A<75 and B=="Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")

    
    
    
    
    
