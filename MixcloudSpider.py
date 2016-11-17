#! /usr/bin/python3

import urllib.request
from urllib.parse import urljoin
import re
from pprint import pprint
from bs4 import BeautifulSoup

base_url = 'https://www.mixcloud.com/LeFtOoO/'
playlist_re = re.compile(r'[+]*([Tt]rack|[Pp]lay)list[+]*')
href_re = re.compile(r'/LeFtOoO/\d{3,}[^/]+/$')


class LeftoSpider(object):

    def listIndex(self, url):
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        entries = soup.findAll("div", class_="column-4 masonry-")
        entries = [entry.find(
            "a", attrs={"m-ref-category": "play"}) for entry in entries]
        index_urls = list([entry['href'] for entry in entries])
        pprint(index_urls)
        return index_urls

    def visitMix(self, url):
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        print("Visited %s" % url)
        return soup

    def findTracklist(self, soup):
        possible_comments = soup.findAll("p", string=playlist_re)
        if not possible_comments:
            pass
        for comment in possible_comments:
            author = comment.find_previous("a", class_="comment-author")
            if author['href'] == "/LeFtOoO/":
                print("HIT! \t Written by %s" % author['href'])
                trackList = comment.find_next("p")
                trackList = [track for track in trackList.stripped_strings]
                pprint(trackList)
                return trackList
            else:
                print("MISS! \t Written by %s" % author['href'])
                continue

    def run(self, mode):
        index_urls = self.listIndex(base_url)
        if mode == "fresh":
            mixSoup = self.visitMix(urljoin(base_url, index_urls[1]))
            trackList = self.findTracklist(mixSoup)
            return trackList
        elif mode == "archive":
            trackList = []
            for index_url in index_urls:
                mixSoup = self.visitMix(urljoin(base_url, index_url))
                trackList.append(self.findTracklist(mixSoup))
            return trackList
        else:
            return print("Set a suitable mode: fresh/archive")