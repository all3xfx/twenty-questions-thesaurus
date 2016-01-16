from scrapy import Spider
import re
import urlparse
from start_urls import urls

class ThesaurusSpider(Spider):
    name = "thesaurus"
    allowed_domains = ["thesaurus.com"]
    start_urls = urls

    def parse(self, response):
        wordname = response.url.split("/")[-1][:-4]
        synonym_body = re.search('Synonyms <span>[\s\S]+<div id="filter-0"><\/div>',
                                 response.body).group()
        relevance3 = re.findall("<.*&quot;relevant-3&quot;.*>", synonym_body)
        relevance2 = re.findall("<.*&quot;relevant-2&quot;.*>", synonym_body)
        relevance1 = re.findall("<.*&quot;relevant-1&quot;.*>", synonym_body)
        num_synonyms = len(relevance3) + len(relevance2) + len(relevance1)
        print "======\n" + str(num_synonyms) + " synonyms found for "+ wordname + ".\n" + "======"
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
                word = re.sub('%20', ' ', word)
                word = urlparse.unquote(word)
                word_list.append(word)


        with open("synonym_logging.txt", "a") as myfile:
            myfile.write(str(num_synonyms) + " synonyms for " + wordname + ":\n" + str(word_list) + "\n")

