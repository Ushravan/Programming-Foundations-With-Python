#Comparing Digits
#Write a program to check if the given two digit number is greater than 25 and its first digit is greater than its second digit.
#Input

#The first line of the input will be a two digit integer
#Output

#Print "True" if the number is greater than 25 and its first digit is greater than its second digit.
#In all other cases print "False".
#Explanation

#When the given number is 24: 
#✖ Greater than 25
#✖ First digit greater than second digit (2 is less than 4)

#When the given number is 42:
#✔ Greater than 25
#✔ First digit greater than second digit (4 is greater than 2)



A = int(input())
B = str(A)
First_greater = (B[0]>B[1])
greater_than = ((A > 25) and First_greater)
print(greater_than)



