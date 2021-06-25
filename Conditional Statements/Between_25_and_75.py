#Between 25 and 75
#Write a program which checks whether the given number N is between 25 and 75.

#Explanation

#For example, if the given input integer is 20, which is not in between 25 and 75, so the output should be False.
#Note: The numbers 25 and 75 are not considered to be in the range.

A = int(input())
B = A > 25 and A < 75
print(B)
