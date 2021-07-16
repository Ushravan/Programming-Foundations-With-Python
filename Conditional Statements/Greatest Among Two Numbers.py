#Greatest Among Two Numbers
#Write a program to print the greatest among the two numbers.
#Input

#The first line of input contains a number.
#The second line of input contains a number.

#Output

#The output should be a single line containing the greatest among the two numbers.

# Explanation

# For example, if the given numbers are 4 and 3, your code should print the greatest number, which is 4.

A = int(input())
B = int(input())
compare = (A > B) 
if compare:
    print(A)
else:
    print(B)
    
