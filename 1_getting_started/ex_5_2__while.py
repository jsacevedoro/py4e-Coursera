'''Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below'''

largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    # Stop the loop when done is written
    if num == "done":
        break
    # Catch non integer values and ignore them
    try:
        num = int(num)    
    except: 
        print("Invalid input")
        continue
    # Update the max and min
    if largest is None:
        largest = num
        smallest = num    
    elif num > largest:
        largest = num
    elif num < smallest:
        smallest = num
    

print("Maximum is", largest)
print("Minimum is", smallest)