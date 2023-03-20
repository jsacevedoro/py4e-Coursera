"""Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below"""

fhandle = open('mbox-short.txt', 'r')
counts = dict()
# Create a histogram in a dictionary
for line in fhandle:
    if line.startswith('From '):
        # Extract the hour
        line = line.split()
        time = line[5]
        time = time.split(':')
        hour = time[0]
        # Store in the dictionary
        counts[hour] = counts.get(hour, 0) + 1

# Turn dict into a list
sorted_by_hour = list(counts.items())
# Sort by key (hour)
sorted_by_hour.sort()

for (hour,count) in sorted_by_hour:
    print(hour, count)
