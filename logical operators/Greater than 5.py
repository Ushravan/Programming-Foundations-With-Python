#Greater than 5
#Write a program to check if both of the given numbers are positive and if atleast one of them is greater than 5
#Note: Zero is not a positive number.
#Input

#First line of the input will be an integer
#Second line of the input will be an integer
#Output

#Print "True" if both the numbers are positive and if atleast one of the numbers is greater than 5.
#In all other cases print "False"
#Explanation

#When the given numbers are -10 and 6: 
#✔ At least one number is greater than 5 (6 is greater than 5)
#✖ Both the numbers are positive (-10 is a negative number.)

#When the given numbers are 10 and 1:
#✔ At least one number is greater than 5 (6 is greater than 5),
#✔ Both the numbers are positive.

A = input()
B = input()
A = int(A)
B = int(B)
greater_than = (A>5) or (B>5)
is_positive = (A>0) and (B>0)
result = (greater_than) and (is_positive)
print(result)





