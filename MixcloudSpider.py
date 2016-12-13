import urllib.request
from urllib.parse import urljoin
import re
from pprint import pprint
from bs4 import BeautifulSoup

AUTHOR = '/LeFtOoO/'
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
        # Changed possible_comment search to first look foor lefto as author
        # TODO: change possible comment iterator to search for tracklist regex
        possible_comments = soup.find_all(
            "a", attrs={"class": "comment-author", "href": AUTHOR})
        if not possible_comments:
            print("No possible comments found")
            return []
        print("Found %d comments with %s as author" %
              (len(possible_comments), AUTHOR))
        print("Checking the first comment")

        for comment in reversed(possible_comments):
            comment_body = comment.find_next("div", class_="comment-body")
            # TODO: Fix the comment_body tracklist search
            # TODO: Make the following nice(r)
            if comment_body:
                track_list_candidates = comment_body.find_all("p")
                print('Found %d possible track lists' % len(track_list_candidates))

                candidates_contents_size = [
                    len(candidate.contents) for candidate in track_list_candidates]
                biggest_candidate = track_list_candidates.pop(
                    candidates_contents_size.index(max(candidates_contents_size)))
                track_list = [track for track in biggest_candidate.stripped_strings]
                return track_list
            else:
                print("Found no good comment body")
                continue

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
