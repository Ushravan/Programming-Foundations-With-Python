#Greatest Among The Powers
#Given two integers a and b, write a program to find the greatest among the powers of each other.
#Input

#The first line of input will contain an integer, (A).
#The second line of input will contain an integer, (B).
#Output

#If AB is greater than BA, print the value of AB.
#In all other cases print the value of BA
#Explanation

#For example, if the given two numbers are 2 and 3. The 23 is 8 and 32 is 9. Your code should print the greatest among the powers, which is 9.


A = int(input())
B = int(input())
case_1 = A ** B > B ** A
if case_1:
    print( A ** B)
else:
    print(B ** A)
    
    
    
