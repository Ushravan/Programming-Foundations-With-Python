#Positive or Negative
#Write a program to find if the given number is positive, negative, or zero.
#Input

#The input will be a single line containing a number.
#Output

#If the given number is greater than zero, print "Positive".
#If the given number is less than zero, print "Negative".
#If the given number is equal to zero, print "Zero".
#Explanation

#For example,if the given number is -12, which is less than 0. So the output should be "Negative".
#Similarly, if the given number is 15, which is greater than zero. So the output should be "Positive"

A = int(input())
greater = A  > 0
if greater:
  print("Positive")
if A<0:
    print("Negative")
if A == 0:
    print("Zero")
    
    
