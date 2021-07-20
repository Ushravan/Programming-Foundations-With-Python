#Lucky Number - 2
#Write a program to print if the given number is divisible by any of the lucky numbers 6, 3, 2 in decreasing order of priority(6 is luckier than 3 and 3 is luckier than 2).
#Print "Number is divisible by" followed by the luckiest number among the above 3 which can divide the number.
#Print "Number is not divisible by 2, 3 or 6" if the number is not divisible by any of them.
#Input

#The input will be a single line containing a positive number.
#Output

#If the given number is divisible by 6, print "Number is divisible by 6".
#If the given number is divisible by 3, print "Number is divisible by 3".
#If the given number is divisible by 2, print "Number is divisible by 2".
#In all other cases print "Number is not divisible by 2, 3 or 6".
#Explanation

#In the example 126 is divisible by 2, 3 and 6
#But 6 takes precedence because 6 is luckiest amongst the three. So the output should be "Number is divisible by 6"

A = int(input())
case_1 = (A%6 == 0)
case_2 = (A%3 == 0)
case_3 = (A%2 == 0)
if case_1 :
    print("Number is divisible by 6")
elif case_2:
    print("Number is divisible by 3")
elif case_3:
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2, 3 or 6")
    
    
    
    
    
