#Compare First Three Characters
#Write a program to check if the first three characters in the two given strings are the same.
#Input

#The first line of input will be a string.
#The second line of input will be a string.
#Output

#Print "True" if the the first three characters in the two given strings are the same.
#In all other cases print "False".
#Explanation

#When the given words are "Apple" and "Application", first three characters in both the strings are the same ("App")

#When the given words are "Android" and "Application", the first three characters in both the strings are different ("And" != "App")


A = str(input())
B = str(input())
print(A[0:3] == B[0:3])




