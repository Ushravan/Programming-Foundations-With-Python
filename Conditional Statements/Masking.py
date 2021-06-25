#Masking
#Write a program that reads a single line of input and prints the first and last characters
#of the given input and prints the asterisk character (*) in place of the remaining characters.

#Explanation

#For example, if the given input word is "qwerty@2020", the output should be "q*********0".
#Note: Observe the number of characters between two ends is equal to the number of asterisk characters (*) in the output.

A = str(input())
length = len(A)
B = A[0]
C = B   +A[length-1]
K = '*'
A[1:length-1] = K
print(A[1:length-1])



