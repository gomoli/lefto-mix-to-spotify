#! /usr/bin/python3

import urllib.request
from urllib.parse import urljoin
import re
from pprint import pprint
from bs4 import BeautifulSoup

BASE_URL = 'https://www.mixcloud.com/LeFtOoO/'
PLAYLIST_RE = re.compile(r'\"?([Tt]rack|[Pp]lay)list\"?')
HREF_RE = re.compile(r'/LeFtOoO/\d{3,}[^/]+/$')


class LeftoSpider(object):

    TRACKLIST = []

    @classmethod
    def list_index(cls, url):
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        entries = soup.find_all("div", class_="column-4 masonry-")
        entries = [entry.find(
            "a", attrs={"m-ref-category": "play"}) for entry in entries]
        index_urls = list([entry['href'] for entry in entries])
        pprint(index_urls)
        return index_urls

    @classmethod
    def visit_mix(cls, url):
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        print("Visited %s" % url)
        return soup

    @classmethod
    def find_tracklist(cls, soup):
        possible_comments = soup.find_all("p", string=PLAYLIST_RE)
        # print(possible_comments)
        if not possible_comments:
            pass
        for comment in possible_comments:
            author = comment.find_previous("a", class_="comment-author")
            if author:
                if author['href'] == "/LeFtOoO/":
                    print("HIT! \t Written by %s" % author['href'])
                    track_list = comment.find_next("p")
                    track_list = [track for track in track_list.stripped_strings]
                    pprint(track_list)
                    return track_list
                else:
                    print("MISS! \t Written by %s" % author['href'])
                    continue
        return []

    @classmethod
    def run(cls, mode):
        index_urls = cls.list_index(BASE_URL)
        if mode == "fresh":
            mix_soup = cls.visit_mix(urljoin(BASE_URL, index_urls[0]))
            track_list = cls.find_tracklist(mix_soup)
            return track_list
        elif mode == "archive":
            for index_url in index_urls:
                mix_soup = cls.visit_mix(urljoin(BASE_URL, index_url))
                cls.TRACKLIST.append(cls.find_tracklist(mix_soup))
            return cls.TRACKLIST
        else:
            return print("Set a suitable mode: fresh/archive")
