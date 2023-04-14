"""In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py. 
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, 
scan for a tag that is in a particular position relative to the first name in the list, 
follow that link and repeat the process a number of times and report the last name you find."""

from urllib.request import urlopen
from bs4 import BeautifulSoup

# Return the n-th anchor tag
def get_tag_in_pos(url, pos):
    # Connect and read the url content
    html = urlopen(url).read()
    # Turn the url content into a soup object
    soup = BeautifulSoup(html, "html.parser")
    # get all anchor tags (anchor tags are tags for hiperlinks)
    tags = soup('a')
    # get the text of the hiperlink
    return tags[pos-1]

# Get the name of tag
def get_name(tag):
    return tag.contents 

# Get the url associated to a anchor tag (hiperlink)
def get_url(tag):
    return tag.get('href')

# open a Url, then follow and print the n-th tag many times
def follow_links(primary_url, position, num_iter):
    url = primary_url
    for _ in range(num_iter)    :
        tag = get_tag_in_pos(url, position)
        print(get_name(tag))
        url = get_url(tag)
    return None


primary_url = input('Enter the url - ')

follow_links(primary_url, 18, 7)