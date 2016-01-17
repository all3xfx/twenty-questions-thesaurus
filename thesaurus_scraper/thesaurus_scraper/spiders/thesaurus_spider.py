from scrapy import Spider
import re
import urlparse
from thesaurus_urls import urls

class ThesaurusSpider(Spider):
    name = "thesaurus"
    allowed_domains = ["thesaurus.com"]
    start_urls = urls
    # start_urls = ["http://www.thesaurus.com/browse/run?s=t"]


    def parse(self, response):
        wordname = response.url.split("/")[-1][:-4]
        print "Scraping: " + wordname
        id_strings = re.findall('id="filter-\d"', response.body)
        max_id = max(map(lambda s: int(s[11:][:-1]), id_strings))
        for i in range(max_id + 1):
            self.search_synonym_body(i, response, wordname)


    def search_synonym_body(self, synonym_id, response, wordname):
        synonym_body = re.search('<div id="synonyms-' + str(synonym_id) + '[\s\S]+<div id="filter-' + str(synonym_id) + '"><\/div>',
                                 response.body).group()
        part_of_speech_txt = re.search('<em class="txt">[\s\S]{1,12}</em>', synonym_body)
        part_of_speech = "noun"
        if part_of_speech_txt:
            part_of_speech = part_of_speech_txt.group()[16:][:-5]
        relevance3 = re.findall("<.*&quot;relevant-3&quot;.*>", synonym_body)
        relevance2 = re.findall("<.*&quot;relevant-2&quot;.*>", synonym_body)
        relevance1 = re.findall("<.*&quot;relevant-1&quot;.*>", synonym_body)
        num_synonyms = len(relevance3) + len(relevance2) + len(relevance1)
        word_list = []
        synonyms = []
        synonyms.extend(relevance3)
        synonyms.extend(relevance2)
        synonyms.extend(relevance1)
        for link in synonyms:
            url = re.search('"http://www.thesaurus.com/browse/[\w|%|\-|\.]+"', link)
            if url == None:
                print link
            if url != None:
                word = url.group()[33:][:-1]
                word = urlparse.unquote(word)
                word_list.append(word)
        # print word_list
        with open("synonym_logging.txt", "a") as myfile:
            myfile.write("(" + wordname + ", " + part_of_speech + ")" "\n" + str(word_list) + "\n\n")