'''Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
The function should return a value. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number.
Do not name your variable sum or use the sum() function'''

# Function definition to compute the payment
def computepay(h, r): 
    # Compute payment
    if h>40:
        extra_time = h-40
        extra_pay = 1.5*extra_time*r
        pay = extra_pay + 40*r
    else:
        pay = h*r 
    return pay

# Function to validate if the parameter is a numeric positive value
def validate_parameter(x):
    # Numeric value validation
    try:
        x = float(x)
    except: 
        print("Please enter numeric values only")
        quit()
    # Positive value validation
    if (x<0):
        print("Please enter a non-negative value")
        quit()   
    return x

# Catch numeric values from user
hours = input("Enter Hours:")
hours = validate_parameter(hours)
rate = input("Enter Rate:")
rate = validate_parameter(rate)

# Function call
p = computepay(hours, rate)

print("Pay", p)