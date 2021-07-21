#Greeting Message
#Write a program to print a greeting message based on the given time.
#Input

#The first line of input will be an integer.
#Output

#If the time is greater than or equal to 4 and less than 12, print "Good Morning".
#If the time is greater than or equal to 12 and less than 16, print "Good Afternoon".
#If the time is greater than or equal to 16 and less than 20, print "Good Evening".
#If the time is greater than or equal to 20 or less than 4, print "Good Night".
#Explanation

#For example, if the given time is 9, your code should print "Good Morning".
#For example, if the given time is 14, your code should print "Good Afternoon".

A = int(input())
if (A < 12) and (A >= 4):
    print("Good Morning")
elif (A >= 12)and(A < 16):
    print("Good Afternoon")
elif (A >=16) and (A < 20):
    print("Good Evening")
elif (A>=20) or (A<4):
    print("Good Night")
    
    
    
    
    
