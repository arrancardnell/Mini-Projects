"""
Author: A.Cardnell
Date: 20th July 2015
Description:

A webcrawler designed to crawl a given webpage and from each page return the
title, url and outgoing links of each.
"""

import requests

from urllib.parse import urlparse, urljoin

from bs4 import BeautifulSoup


class Crawler(object):
    """Main class for web crawler."""

    def get_url(self):
        print('Enter a URL to scan: ')
        chosen_url = input()
        if not chosen_url.startswith('http://'):
            chosen_url = 'http://' + chosen_url  # 'http://' appended for Beautiful Soup
        return chosen_url

    def get_text(self, txt_url):
        """Convert the URL to Beautiful Soup text."""
        
        try:
            r = requests.get(txt_url)
            soup = BeautifulSoup(r.content) 
        except:
            print('The text from this URL cannot be extracted.')
        return soup

    def web_crawler(self, webtext, base):
        """Crawls one page deep and prints the results to the console."""
        
        self.webtext = webtext
        self.base = base

        visited = []
        for link in self.webtext.find_all('a', href=True):  # finds all the links in the Beautiful Soup text

            link['href'] = urljoin(self.base, link['href'])

            if link['href'] not in visited and link['href']:
                title = '\nTitle: ' + link.text
                URL = 'URL: ' + link['href']
                print(title)
                print(URL)
                visited.append(link['href'])
                if link['href'].startswith(self.base):  # avoid crawling external sites
                    outgoing_visited = []
                    outgoing_title = 'Outgoing link:'
                    print(outgoing_title)
                    for outgoing in self.get_text(link['href']).find_all('a', href=True):
                        outgoing['href'] = urljoin(self.base, outgoing['href'])
                        if outgoing['href'] not in outgoing_visited:
                            outgoing_links = '\t' + outgoing['href']
                            print(outgoing_links)
                            outgoing_visited.append(outgoing['href'])

    def crawl(self):
        """Crawler setup method."""
        
        user_url = self.get_url()
        text_url = self.get_text(user_url)
        base_url = 'http://' + urlparse(user_url).netloc + '/'  # create the base URL from the chosen URL

        try:
            self.web_crawler(text_url, base_url)
        except:
            print('That\'s not a valid URL!')

if __name__ == "__main__":
    Crawler = Crawler()
    Crawler.crawl()
