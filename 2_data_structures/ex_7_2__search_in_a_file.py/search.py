"""Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution."""

# Get file name and create connection to read it
file_name = input("Enter the file name: ")
file_handle = open(file_name, 'r')

counter = 0 
total = 0

for line in file_handle:
    pos1 = line.find("X-DSPAM-Confidence:")
    # When the line doesn't contain that substring, the output is -1
    if pos1 != -1:
        counter += 1
        string = line[pos1+1:]
        string = string.rstrip()
        # Get only the number
        pos2 = string.find(":")
        num = string[pos2+1:]
        num = float(num)
        total += num

avg = total/counter
print("Average spam confidence:",avg)



