"""Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""

fhandle = open('mbox-short.txt', 'r')

# Store email and ocurrencies in a dict
counts = dict()
for line in fhandle:
    if line.startswith('From '):
        # Get the email string
        line = line.split()
        email = line[1]
        # If the email key doesn't exist in the dict, create it and assign the deffault value 0, else sum 1.
        counts[email] = counts.get(email,0) + 1

# Find email with more ocurrency
maximum = 0
max_mail = ""
for mail, count in counts.items(): 
    if count >= maximum:
        maximum = count
        max_mail = mail

print(max_mail, maximum)