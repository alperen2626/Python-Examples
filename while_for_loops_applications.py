"""
Printing the even numbers between two integer values
which assigned by the user.

"""
min_number=int(input("Enter the  lower limit: "))
max_number=int(input("Enter the  upper limit: "))
for x in range(min_number+1,max_number):
    if(x%2==0):
        print(x,end="-")
    else:
        continue

print()



#***************************************************************************
"""
Using while loop find the random number generated by computer
Note:use import random to generate random number

"""
import random
xnum=random.randint(1,100)

num=0

while(num!=xnum):
    num=int(input("Please Enter nmber between 1 and 100:  "))
    if(num>xnum):
        print(f"Please enter lower than  {num} value")

    elif (num< xnum):
        print(f"Please enter greater than {num} value")

    else:
        print(f"You find it congratulations entered value is {num} and random number is {xnum} ")

#***************************************************************************
