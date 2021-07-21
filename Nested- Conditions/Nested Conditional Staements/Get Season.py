Get Season
Write a program to find season for the given month number.
Input

The first line of input will contain an integer that indicates the number of the month.
If the given number of the month is 3, that indicates March month.
Output

If the given month is either November or December or January, print "Winter".
If the given month is either February or March, print "Spring".
If the given month is either April or May or June print "Summer".
If the given month is either July or August, print "Rainy".
If the given month is either September or October, print "Autumn".
Explanation

For example, if the given month is 1, which indicates January month, the output should be "Winter".
Similarly, if the given month is 4, which indicates April month, the output should be "Summer".

Month = int(input())
if (Month==12)or(Month==11)or(Month==1):
    print("Winter")
elif (Month ==3)or(Month==2):
    print("Spring")
elif (Month==6) or(Month==4):
    print("Summer")
elif (Month ==8)or(Month==7):
    print("Rainy")
else:
    print("Autumn")
    
    
    
    
    
    
