#Relation Between Two Numbers
#Given two integers A and B, write a program to print the relation between the two numbers.
#Input

#The first line of input will contain an integer.
#The second line of input will contain an integer.
#Output

#If A is equal to B, print "A == B".
#If A is greater than B, print "A > B".
#If A is less than B, print "A < B".
#Explanation

#For example, if the given numbers are A is 3 and B is 4, where 3 is less than 4. So the output should be "A < B".
#For example, if the given numbers are A is 4 and B is 4, where 4 is equal to 4. So the output should be "A == B".

A = int(input())
B = int(input())
if A == B :
    print("A == B")
elif A>B :
    print("A > B")
else:
    print("A < B")
    
    
    
    
    
    
