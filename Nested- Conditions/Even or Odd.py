#Even or Odd
#Write a program to check if the given number is even or odd.
#Input

#The input will be a single line containing an integer.
#Output

#If the given number is even, print "Even". If it is odd, print "Odd".
#Explanation

#For example, if the given number is 4, which is divisible by 2, the output should be "Even".

#Whereas, if the given number is 3, which is not divisible by 2, the output should be "Odd".

integer = int(input())
is_even = (integer%2) 
if (is_even == 0):
    print('Even')
else:
    print('Odd')
    
    
    
    
    
