import platform
import os
import errno
import urllib
import urllib3
import webbrowser
from urllib.request import urlopen
import pypandoc
import bs4
import requests

##############################################################################
# webbrowser.open(url_name)
# webbrowser.open('http://www.duckduckgo.com')
##############################################################################

os_name = platform.system()
if os_name == "Windows":
    from docx import Document
    #from docx.shared import Inches
    from pypandoc import *

from bs4 import BeautifulSoup

if os_name == "Windows":
    url_link_dbg_fle = ('..\dbgtestdocs\webtext0.txt', '..\dbgtestdocs\webtext.txt1')
else:
    url_link_dbg_fle = ('../dbgtestdocs/webtext0.txt', '../dbgtestdocs/webtext.txt1')


##########################################################
# static function which used only inside this module
##########################################################

################################################################################
# define a url
################################################################################
def html_to_text ( file_name, data ):
    d_dir = os.path.dirname(file_name)
    if not os.path.isdir(d_dir):
        os.mkdir(os.path.dirname(file_name))
    with open(file_name, 'w', encoding="utf8") as fulltext:
        fulltext.write(data)


class UrlLinkUtility:
    def __init__ ( self, home_url, index_url, logging_util ):
        self.home_page_url = home_url
        self.index_page_url = index_url
        self.select_url = ""
        self.open_page = ""
        self.url_list = []
        self.logging = logging_util

    def find_match_url ( self, page, match_str ):
        html_to_text(url_link_dbg_fle[0], page)
        final_quote = 0
        while True:
            start_link = page.find('href="')
            if start_link == -1:
                return None, 0
            start_quote = page.find('"', start_link)
            end_quote = page.find('"', start_quote + 1)
            url = page[start_quote + 1: end_quote]
            page = page[end_quote:]
            final_quote += end_quote
            if url.find(match_str) != -1:
                break
        return url, final_quote

    def open_an_url_link ( self, url_name ):
        url_name = self.index_page_url + url_name
        webbrowser.open_new(url_name)  # for debug purpose, will comment out after
        try:
            response = urllib.request.urlopen(url_name)
        except urllib.error.HTTPError:
            self.logging.dbg_logging("ERROR::Missing page 404 URL link {url_name}".format(url_name=url_name))
            urllib.request.urlcleanup()
            return False
        except urllib.error.URLError:
            self.logging.dbg_logging("ERROR::link {url_name} broken".format(url_name=url_name))
            urllib.request.urlcleanup()
            return False

        html = response.read()
        # parse html
        response = requests.get(url_name)
        self.open_page = str(BeautifulSoup(response.content, "lxml"))
        return True

    def build_url_link_list ( self, request_str ):
        self.url_list.clear()
        page = self.open_page
        while True:
            url, n = self.find_match_url(page, request_str)
            if url:
                url = self.home_page_url + url
                self.url_list.append(url)
                page = page[n:]
            else:
                break
        self.logging.dbg_logging("INFO::Total list elements:" + str(len(self.url_list)))

    def extract_text_from_xml(self):
        # response = requests.get(self.select_url)
        html = urlopen(self.select_url).read()
        soup = BeautifulSoup(html, 'html.parser')
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()  # rip it out
        # get text
        text = soup.get_text()
        return text

