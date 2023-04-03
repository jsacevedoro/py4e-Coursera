'''Find all the integer numbers in the text, sum them and print it'''

import re 

fhand = open('regex_sum_1770331.txt')
sum = 0

for line in fhand:
    numbers = re.findall("[0-9]+", line)
    for num in numbers:
        num = int(num)
        sum += num

print(sum)