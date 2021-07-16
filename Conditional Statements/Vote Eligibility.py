#Vote Eligibility
#A person is eligible to vote if his/her age is at least 18 years. Write a program that checks if a person is eligible to vote based on the person's age.
#Input

#The input will be a number denoting the person's age in years.
#Output

#If the person's age is at least 18, print "Eligible".
#In all other cases, print "Not Eligible".
#Explanation

#A person is eligible to vote if his/her age is 18 years or above.
#For example, if the person's age is 15, which is below 18. So the output should be "Not Eligible".
#Whereas if the person's age is 21, which is above 18. So the output should be "Eligible".

A = int(input())
if A >= 18 :
    print("Eligible")
else:
    print("Not Eligible")
    
    
    
    
    
