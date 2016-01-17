from scrapy import Spider
import re
from dictionary_urls import urls
from HTMLParser import HTMLParser

class ThesaurusSpider(Spider):
    name = "dictionary"
    allowed_domains = ["dictionary.com"]
    # start_urls = ["http://www.dictionary.com/list/a/1"]
    start_urls = urls


    def parse(self, response):
        letter = response.url.split("/")[-2]
        number = response.url.split("/")[-1]
        print "Scraping: " + letter + " " + number
        words_html = re.findall('<span class="word">[\s\S]{1,80}</span>', response.body)
        words = map(lambda s : s[19:][:-7] , words_html)
        h = HTMLParser()
        words = map(lambda s : h.unescape(s) , words)
        words = filter(lambda s : type(s) == str, words)
        # print words
        word_string = reduce(lambda x,y : x + "\n" + y , words) + "\n"
        with open("scraped_words.txt", "a") as myfile:
            myfile.write(word_string)


