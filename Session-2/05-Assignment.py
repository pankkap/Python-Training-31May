# Assignment-1
# Take two no. from computer and perform addition and subtraction of those numbers

# x = int(input("Enter First Number: "))
# y = int(input("Enter second Number "))

# z = x + y
# print("Result:", z)


# Assignment-2
# Marksheet
# Write a program that prompts the user to enter a numerical grade (0-100) and prints a corresponding letter grade based on the following criteria:
# 1. Take input from user ("Enter your Percentage")
# 90 or above: "A"
# 80-89: "B"
# 70-79: "C"
# 60-69: "D"
# Below 60: "F"

per = float(input("Enter your Percentage: "))

if(per>=90 and per<=100):
    print("You are having Grade-A")
elif(per>=80 and per<90):    
    print("You are having Grade-B")
elif(per>=70 and per<80):    
    print("You are having Grade-C")
elif(per>=60 and per<70):    
    print("You are having Grade-D")
elif(per<60 and per>=0):    
    print("You are having Grade-F")
else:
    print("Enter correct Percentage")


# Find the largest number from below numbers
a = 100
b = 31
c = 17
