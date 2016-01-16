from scrapy import Spider
import re


class ThesaurusSpider(Spider):
    name = "thesaurus"
    allowed_domains = ["thesaurus.com"]
    start_urls = ["http://www.thesaurus.com/browse/community?s=t", "http://www.thesaurus.com/browse/bob?s=t"]

    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
        synonym_body = re.search('Synonyms <span>[\s\S]+<div id="filter-0"><\/div>',
                                 response.body).group()
        ripped_links = re.findall("<.*&quot;relevant-2&quot;.*>", synonym_body)
        print "======\n" + str(len(ripped_links)) + " synonyms found.\n" + "======"
        with open("Output.txt", "w") as text_file:
            text_file.write(str(map(lambda s: s[:60], ripped_links)))
        word_list = []
        for link in ripped_links:
            url = re.search('"http://www.thesaurus.com/browse/\w+"', link)
            if url == None:
                print link
            if url != None:
                word = url.group()[33:][:-1]
                word_list.append(word)
        print word_list