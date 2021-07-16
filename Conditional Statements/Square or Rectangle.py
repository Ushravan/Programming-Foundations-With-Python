#Square or Rectangle
#Given the length and breadth of a box, check if it is a Rectangle or Square.
#Input

#The first line of input will contain the length of the box.
#The second line of input will contain the breadth of the box.
#Output

#If the given length and breadth are equal, print "Square". In all other cases, print "Rectangle".
#Explanation

#For example, if the given length is 6, and the given breadth is 6, the length and breadth are equal. So the output should be "Square".
#Similarly, if the given length is 5, and the breadth is 10, the length and breadth are not equal. So the output should be "Rectangle".

A = int(input())
B = int(input())
result = (A == B)
if result:
    print("Square")
else:
    print("Rectangle")
    
    
