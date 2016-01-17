
filename = 'C:\\Users\\pgirardet\\Documents\\HackRice\\shorter_words.txt'
url = "http://www.thesaurus.com/browse/"
links = []
with open(filename) as f:
    for word in f:
        word = word.strip()
        into_uni = word.decode('unicode-escape')
        into_html = into_uni.encode('ascii', 'xmlcharrefreplace')
        links.append(url + into_html + "?s=t")

urls = links