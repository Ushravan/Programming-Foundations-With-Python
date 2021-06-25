#Validate Password
#Write a program to check if the given string is a valid password or not. A string is considered as a valid password if the number of characters present is greater than 7.

#Explanation

#For example, if the given input is "passwd", it has only 6 characters (less than 7). So the output should be False.


A = str(input())
B = len (A)
greater_than = B > 7
if greater_than:
    print('True')
else:
    print('False')
    
    
    
    
