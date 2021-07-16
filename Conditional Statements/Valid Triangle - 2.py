#Valid Triangle - 2
#Given the lengths of three sides of a triangle, write a program to check whether the triangle is valid or not.
##For a triangle to be valid, the sum of lengths of any two sides of the triangle must be greater than the third side.
#Input

#The first line of input will contain the first side of the triangle.
#The second line of input will contain the second side of the triangle.
#The third line of input will contain the third side of the triangle.
#Output

#If the sum of the lengths of any two sides of the triangle is greater than the third side, print "It's a Triangle". In all other cases, print "It's not a Triangle".
#Explanation

#For example, if the first side is 4, the second side is 5, and the third side is 3, then the sum of any two sides is greater than the third side:
 #  4 + 5 > 3
 #  5 + 3 > 4
 #  3 + 4 > 5
#So the output should be "It's a Triangle".

A = int(input())
B = int(input())
C = int(input())
Greater = (A+B>C) and (B+C>A) and (A+C>B)
if Greater:
    print("It's a Triangle")
else:
    print("It's not a Triangle")
    
    
    
