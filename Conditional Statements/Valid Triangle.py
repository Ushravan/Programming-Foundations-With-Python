#Valid Triangle
#Given three angles of a triangle, write a program to check whether the triangle is valid or not. A triangle is valid if the sum of its three angles is equal to 180 degrees.
#Input

#The first line of input will contain the first angle of the triangle.
#The second line of input will contain the second angle of the triangle.
#The third line of input will contain the third angle of the triangle.
#Output

#If the sum of the three angles is equal to 180, print "It's a Triangle". In all other cases, print "It's not a Triangle".
#Explanation

#For example, if the first angle is 80, the second angle is 90, and the third angle is 100. Therefore the sum of the three angles(80 + 90 + 100) is 270, 
#which is not equal to 180. So the output should be "It's not a Triangle".
#Similarly, if the first angle is 60, the second angle is 60, and the third angle is 60. Therefore the sum of the three angles(60 + 60 + 60) is 180, 
#which is equal to 180. So the output should be "It's a Triangle".

A = int(input())
B =int(input())
C = int(input())
Sum = (A*B*C)
if (Sum == 180):
    print("It's Triangle")
else:
   print("It's not Triangle")
    
    
    
    
    
