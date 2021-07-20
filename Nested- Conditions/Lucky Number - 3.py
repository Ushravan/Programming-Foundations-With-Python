#Lucky Number - 3
#Given a two-digit number, print "Lucky Number" if any of the following conditions are satisfied
#	1. The number is a multiple of 9
#	2. One of the digits is 9
#Print "Unlucky Number" in all other cases.
#Input

#The first line of input will contain an integer.
#Output

#If any of the above conditions are satisfied, print "Lucky Number".
#In all other cases, print "Unlucky Number".
#Explanation

#For example, if the given number is 18, which is a multiple of 9, the output should be "Lucky Number".

#Whereas, if the given number is 13, which does not satisfy any of the conditions, the output should be "Unlucky Number".


A =int(input())
B = str(A)
case_1 = (A % 9 == 0) or (int(B[0])==9) or (int(B[1])==9)
if case_1:
    print("Lucky Number")
else:
    print("Unlucky Number")
    
    
    
