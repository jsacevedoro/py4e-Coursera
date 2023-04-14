"""The program will prompt for a URL, read the XML data from that URL using urllib 
and then parse and extract the comment counts from the XML data, 
compute the sum of the numbers in the file"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

def prompt_url():
    # Prompt url from user
    url = input('Please enter the url -')
    if len(url)>1:
        return url
    else:
        # URL with the sample data
        default_url = "http://py4e-data.dr-chuck.net/comments_42.xml"
        print("Running the program with the default url with the sample data")
        return default_url


def get_data_from_url(url):
    # Create the conection with the url
    u_handle = urllib.request.urlopen(url)
    # Get the data in UTF-8 format
    data = u_handle.read()
    # Turn the data into python string
    data = data.decode()
    return data


def get_sum_of_counts(data):
    sum = int(0)
    # Transform string-data to a tree-structure
    tree = ET.fromstring(data)
    # Find all the tags named count, no matter its father
    counts_list = tree.findall('.//count')
    for count in counts_list:
        # get the text inside the tag, which is the number and then turn into integer
        num = int(count.text)
        sum += num
    return sum


def main():
    url = prompt_url()
    data = get_data_from_url(url)
    sum = get_sum_of_counts(data)
    print("The sum of all numbers is:", sum)

main()



