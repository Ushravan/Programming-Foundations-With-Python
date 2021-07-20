#Special Eleven
#A number is called Special Eleven, if it is a multiple of 11 or if it is one more than a multiple of 11. Write a program to check if the given number is a Special Eleven number.
#Input

#The input will be a single line containing an integer.
#Output

#If the given input satisfies the above conditions, print "Special Eleven". In all other cases print "Normal Number".
#Explanation

#For example, if the given number is 22, which is a multiple of 11, the output should be "Special Eleven".

#Similarly, if the given number is 23, which is one more than a multiple of 11, the output should be "Special Eleven".

#Whereas, if the given number is 15, which does not satisfy any of the conditions, the output should be "Normal Number".

A = int(input())
case_1 = (A%11 == 0) or (A%11 == 1)
if case_1:
    print("Special Eleven")
else:
    print("Normal Number")
    
    
    
