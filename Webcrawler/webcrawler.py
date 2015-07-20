"""
Author: A.Cardnell
Date: 20th July 2015
Description:

A webcrawler designed to crawl a given webpage
and from each page return the title, url and
outgoing links of each.
"""

import sys
import platform
import os
import requests
from urllib.parse import urlparse
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# function to get the URL from the user. Adds 'http://' if user does not include in the address
def get_url():
    print('Enter a URL to scan: ')
    chosen_url = str(input())
    if 'http://' not in chosen_url: # add 'http://' so it text can be extracted
        chosen_url = 'http://' + chosen_url
    return chosen_url

# function to convert selected url to BeautifulSoup text format
def get_text(txt_url):
    try:
        r = requests.get(txt_url)
        soup = BeautifulSoup(r.content)
    except:
        print('The text from this URL cannot be extracted')
    return soup            

# function to crawl selected website and return title, url and outgoing links on each page
def web_crawler(webtext, base):
    try:
        for link in webtext.find_all('a', href=True): # find all the weblinks on the page
            link['href'] = urljoin(base, link['href']) # create full http:// address
            if link['href'] not in visited and link['href']: # check not already visted and valid link
                title = '\nTitle: ' + link.text
                URL = 'URL: ' + link['href']
                print(title)
                print(URL)
                visited.append(link['href']) # add to visited so it doesn't revisit same links
                if file_name: # if the user requested saving, write the title and url to the file
                    WriteToFile(save_directory, title)
                    WriteToFile(save_directory, URL)
                if base in link['href']: # check site contains starting URL, avoids going into other domains
                    outgoing_visited = []
                    outgoing_title = 'Outgoing links:'
                    print(outgoing_title)
                    if file_name: 
                        WriteToFile(save_directory, outgoing_title)
                    for outgoing in get_text(link['href']).find_all('a', href=True): #find the outgoing links on the current page
                        outgoing['href'] = urljoin(base, outgoing['href']) #create the full outgoing link address
                        if outgoing['href'] not in outgoing_visited: # check outgoing link hasn't already been shown for that page
                            outgoing_links = '\t' + outgoing['href']
                            print(outgoing_links)
                            outgoing_visited.append(outgoing['href']) # don't include the same link if it appears multiple times on the same page
                            if file_name:
                                WriteToFile(save_directory, outgoing_links)
    except:
        print("The text was not formatted before attempting to crawl.")

def WriteToFile(filename, text):
    file = open(filename, "a")
    file.write(text + '\n')
    file.close()

#  function for that checks if the user wants to save the results in a text output and returns the required file name
def create_file():
    print("\nDo you want to save this to a file? (Yes/No)")
    print("\nIf yes, the output will be printed to the console \nand saved in a text file to the desktop.")
    print("\nIf no, the output will be printed to the console only.")
    answer = input("\n> ").lower()
    if answer in ("yes" or "y"):
        f_name = input("\nPlease give the file a name: ")
        return f_name
    else:
        return None

# function to determine if the file will be saved on Windows or Linux
def os_check(version):
    username = os.environ.get( "USERNAME" )
    if 'Windows' or 'windows' in version:
        path = ('C:/Users/' + username + '/Desktop/')
    elif 'Linux' or 'linux' in version:
        path = '/home/Documents/'
    else:
        print("OS version not supported.")
    return path

# create a directory to store the file if required
def create_directory(path, site_name):
    directory_name = (str(site_name))
    try:
        os.makedirs(path + directory_name) # create the directory on the desktop with the name requested by the user
    except:
        print("Cannot create the directory")
    return directory_name

user_url = get_url() # get the required URL from the user
base_url = 'http://' + urlparse(user_url).netloc # return just the base component of the user url (so that you can use it to prevent crawler from searching externally)
visited = []
save_directory = None
os_version = platform.platform() # check which operating system user is using

file_name = create_file()
if file_name:
    save_directory = os_check(os_version) + create_directory(os_check(os_version), file_name + '\\') + file_name + '.txt' # create a text file for the output with the users requested file name

try:
    web_crawler(get_text(user_url), base_url)
except:
    print('That\'s not a valid URL!')
