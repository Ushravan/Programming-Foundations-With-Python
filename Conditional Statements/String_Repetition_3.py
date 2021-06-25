#String Repetition 3
#Given a word and a number (N), write a program to print the last three characters of the word N times in a single line.

#Explanation

#For example, if the given input is "Transport" and the given number is 2.
#The last three characters of the given word are "ort", which have to be repeated 2 times, so the output should be "ortort"


Word =input()
N = int(input())
length = len(Word)
start_from = length-3
repeatation_of_characters = Word[start_from:]
massage = repeatation_of_characters*N
print(massage)



