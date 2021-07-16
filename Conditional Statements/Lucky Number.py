#Lucky Number
#Given two integers, they are considered a lucky pair if any one of them is 6 or if their sum or difference is equal to 6.
#Input

#The first line of input contains a number.
#The second line of input contains a number.
#Output

#If the given conditions are satisfied, print "Lucky".  In all other cases, print "Not Lucky".
#Explanation

#For example, if the given numbers are 6 and 1. One of the given two numbers is 6. So the output should be "Lucky".
#Whereas, if the given numbers are 3 and 2, they do not satisfy any of the conditions. So the output should be "Not Lucky".

A = int(input())
B = int(input())
Equal = (A+B==6) or ((A == B)==6) or (B-A==6) or (A-B ==6)
if Equal == 6 :
    print("Lucky")
else:
    print("Not Lucky")
    
    
    
    
