from scrapy import Spider
import re
import urlparse

class ThesaurusSpider(Spider):
    name = "thesaurus"
    allowed_domains = ["thesaurus.com"]
    start_urls = ["http://www.thesaurus.com/browse/community?s=t", "http://www.thesaurus.com/browse/bob?s=t",
                  "http://www.thesaurus.com/browse/people?s=t", "http://www.thesaurus.com/browse/machiavellian?s=t",
                  "http://www.thesaurus.com/browse/fantastic?s=t"]

    def parse(self, response):
        wordname = response.url.split("/")[-1][:-4]
        synonym_body = re.search('Synonyms <span>[\s\S]+<div id="filter-0"><\/div>',
                                 response.body).group()
        relevance3 = re.findall("<.*&quot;relevant-3&quot;.*>", synonym_body)
        relevance2 = re.findall("<.*&quot;relevant-2&quot;.*>", synonym_body)
        relevance1 = re.findall("<.*&quot;relevant-1&quot;.*>", synonym_body)
        print "======\n" + str(len(relevance3) + len(relevance2) + len(relevance1)) \
              + " synonyms found for "+ wordname + ".\n" + "======"
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
        print word_list