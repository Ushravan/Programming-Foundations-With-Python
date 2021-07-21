Name of the polygon
Given the number of sides, write a program to print the name of the polygon.
Input

The first line of input will contain an integer.
Output

If the given number of sides is less than 3, print "Not Polygon".
If the given number of sides is equal to 3, print "Triangle".
If the given number of sides is equal to 4, print "Quadrilateral".
If the given number of sides is equal to 5, print "Pentagon".
If the given number of sides is greater than 5, print "Big Polygon".
Explanation

For example, if the given number of sides is 4, the output should be "Quadrilateral".
Similarly, if the given number of sides is 2, the output should be "Not Polygon".


A = int(input())
if A<3:
    print("Not Polygon")
elif A==3:
    print("Triangle")
elif A==4:
    print("Quadrilateral")
elif A == 5:
    print("Pentagon")
else:
    print("Big Polygon")
