# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number

hours = input("Enter Hours: ")
rate = input("Enter the Rate: ")

# Turn input strings to numeric if they are valid
try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Enter numeric values only")
    quit()

# Calculate pay considering the condition of hours up to 40
if hours > 40:
    diff = hours-40
    extra_pay = diff*rate*1.5
    pay = extra_pay + 40*rate
else:
    pay = hours*rate
    
print(pay)