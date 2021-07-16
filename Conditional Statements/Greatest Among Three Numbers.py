#Greatest Among Three Numbers
#Write a program which prints the greatest among the given three numbers.
#Input

#The first line of input will contain a number.
#The second line of input will contain a number.
#The third line of input will contain a number.
#Output

#The output should be a single line containing the greatest among the three numbers.
#Explanation

#For example, if the given numbers are 2, 5, and 7. Your code should print the greatest number, which is 7.

A = int(input())
B = int(input())
C = int(input())
case_1 = (A>B) and (A > C) 
case_2 = (B>A) and (B>C)
case_3 = (C>A)and(C>B)
if case_1:
    print(A)
if case_2:
    print(B)
if case_3:
    print(C)
if (case_1)==(case_2)==(case_3):
    print(A)
    
    
