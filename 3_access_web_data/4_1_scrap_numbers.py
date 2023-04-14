"""The program will use urllib to read the HTML from the data files below, 
and parse the data, extracting numbers and compute the sum of the numbers in the file"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter the url - ')

# Connect and read the url content
html = urlopen(url).read()
# Turn the url content into a soup object
soup = BeautifulSoup(html, "html.parser")

# search for span tag
tags = soup('span')

# Sum all numbers
sum = 0
for tag in tags:
    # Get the content of span mark, which in this case is the number
    num = tag.contents[0]
    sum += int(num)

print(sum)

