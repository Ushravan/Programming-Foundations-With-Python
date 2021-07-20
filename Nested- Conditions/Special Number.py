#Special Number
#Write a program to read a single line of input, which is a two-digit integer and
#Print "Special Number" if any one of the following conditions are satisfied
#	1. The sum of digits is 7	2. One of the digits is 7
#	3. The number is a multiple of 7
#Print "Normal Number" in all other cases
#Input

#The first line of input contains a two-digit integer.
#Output

#If the given input satisfies the above conditions, print "Special Number". In all other cases print "Normal Number".
#Explanation

#For example, if the given two-digit integer is 67.
#As one of its digits is 7, the output should be "Special Number".

#Whereas, if the given two-digit integer is 36.
#As it does not satisfy any of the above conditions, the output should be "Normal Number".

A = int(input())
B = str(A)
length = len(B)
case_1 = (( int(B[0]) + int(B[1]) )==7) or (int(B[0]) ==7 or int(B[1])==7) or ((A%7) == 0)
if case_1 :
    print("Special Number")
else:
    print("Normal Number")
    
    
    
    
    
    
