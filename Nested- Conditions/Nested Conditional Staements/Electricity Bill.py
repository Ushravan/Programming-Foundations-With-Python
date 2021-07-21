Electricity Bill
In this problem, you need to write a program to calculate the electricity bill for a household, based on the units of electricity the household consumed. The price for unit varies based on the slab. The charges per unit for different slabs are as mentioned below:
For the first 50 units (0-50), the charge is 2/unit
For the next 100 units (51-150), the charge is 3/unit
For the next 100 units (151-250), the charge is 5/unit
For above 250 units (251 and above), the charge is 8/unit
Apart from these charges, there is also an additional surcharge of 20% on the total amount is added to the bill.
Input

The input will be a single line containing an integer. 
Output

The output should be a single line containing the calculated bill amount. 
Explanation

For example, if the given number of units is 50.

Charges 2/unit for 0 to 50 units   =>  50 x 2   = 100
Charges 3/unit for 51 to 150 units =>   0 x 3   =   0
Charges 5/unit for 151 to 250      =>   0 x 5   =   0
Charges 8/unit for 251 and above   =>   0 x 8   =   0
-----------------------------------------------------
Total                              =>             100 
Surcharge (20 % of Bill)           => 100 x 0.2 =  20
-----------------------------------------------------
Bill                               =>             120
-----------------------------------------------------

So the total bill should be 120.0


For example, if the given number of units is 200.

Charges 2/unit for 0 to 50 units   =>  50 x 2   = 100
Charges 3/unit for 51 to 150 units => 100 x 3   = 300
Charges 5/unit for 151 to 250      =>  50 x 5   = 250 
Charges 8/unit for 251 and above   =>   0 x 8   =   0
-----------------------------------------------------
Total                              =>             650 
Surcharge (20 % of Bill)           => 650 x 0.2 = 130
-----------------------------------------------------
Bill                               =>             780
-----------------------------------------------------

So the total bill should be 780.0



A = int(input())
Total=0 

if A< 50:
   Total= A*2
   
elif A<150:
    Total = (2*50)+(3*(A-50))
    
elif (A<250):
   Total = (2*50)+(3*100)+(5*(A-150)) 
   
elif A>=250:
    Total = (2*50)+(3*100)+(5*100)+(8*(A-250))
    
extra_chrages= (Total*0.2)

total_bill=(Total+extra_chrages)

print(total_bill)


