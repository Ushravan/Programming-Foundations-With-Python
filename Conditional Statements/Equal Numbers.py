#Equal Numbers
#Write a program to check if the given two numbers are equal.
#Input

#The first line of input contains a number.
#The second line of input contains a number.
#Output

#If the given numbers are equal, print "Equal". In all other cases, print "Not Equal".
#Explanation

#For example, if the first number is 5 and the second number is 5. Since both the given numbers are equal. So the output should be "Equal".
#Whereas, if the first number is 10 and the second number is 5, both the numbers are not equal. So the output should be "Not Equal".

A = int(input())
B = int(input())
Result = (A == B)
if Result:
    print("Equal")
else:
    print("Not Equal")
    
    
    
    
