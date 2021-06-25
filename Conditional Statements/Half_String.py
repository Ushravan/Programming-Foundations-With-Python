#Half String

# Write a program which prints the first half of the given input string.
# You can assume that the length of the input string will always be an even number.

# Explanation

#For example, if the given input is "Amazon", the first half of it is "Ama".


A = input()
Length = len(A)
B = int(Length)-int(Length/2)
Half =A[0:B]
print(Half)




