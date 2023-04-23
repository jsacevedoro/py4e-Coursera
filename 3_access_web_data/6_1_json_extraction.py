"""The program will prompt for a URL, read the JSON data from that URL using urllib 
and then parse and extract the comment counts from the JSON data, 
compute the sum of the numbers in the file and enter the sum below"""

import urllib.request
import json

def prompt_url():
    # Prompt url from user
    url = input('Please enter the url -')
    if len(url)>1:
        return url
    else:
        # URL with the sample data
        default_url = "http://py4e-data.dr-chuck.net/comments_42.json"
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
    # Turn json string into a dictionary
    data_dict = json.loads(data)
    # Sum the counts according to json structure
    for item in data_dict['comments']:
        num = int(item['count'])
        sum += num
    return sum


def main():
    url = prompt_url()
    data = get_data_from_url(url)
    sum = get_sum_of_counts(data)
    print("The sum of all numbers is:", sum)

main()
