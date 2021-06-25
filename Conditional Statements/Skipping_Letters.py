#Skipping Letters
#You're given a word and an index position of a character. You need to write a program that prints the given word without the character at the given index.

#Explanation

#For example, if the given word is "Combine", the character at the index location 4, is "i", so the output without the character at the given index location is "Combne"

A = input()
index =int(input())
B = A[:index]
C = A[index+1:]
print(B+C)


