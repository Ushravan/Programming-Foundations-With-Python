#Exam Result
#Write a program that reads the student's marks as input and prints PASS or FAIL.If the student has scored more than 50, print PASS.
#In all other cases print FAIL.

#Explanation

#In the given example, the student's marks are 85, which is more than 50, so the result should be PASS.
#Similarly, if the marks are 45, the result should be FAIL.

A = int(input())
score = A > 50
if score:
    print('PASS')
else:
    print('FAIL')

    
    
