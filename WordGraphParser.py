import json
import io
from collections import defaultdict
import re
import ast
from OrderedSet import OrderedSet
import time

"""
Class for initializing a word association graph from parsed scraped synonym data, returned as a dictionary.
"""

def merge_lists(lists):
    indices = [0]*len(lists)
    current_list = 0
    merged_list = []
    list_lengths = map(lambda x : len(x), lists)
    while True:
        if list_lengths == indices:
            break
        if indices[current_list] == len(lists[current_list]):
            current_list += 1
            current_list %= len(lists)
            continue
        num = lists[current_list][indices[current_list]]
        indices[current_list] += 1
        merged_list.append(num)
        if list_lengths == indices:
            break
        current_list += 1
        current_list %= len(lists)
    return merged_list

# lists = [[1]]
# print merge_lists(lists)
# lists = [[1,7],[2,5,8],[3,6,9]]
# print merge_lists(lists)

def synonym_block_parser(block):
    header = re.search("\(\w+, \w+\)", block).group()
    body = re.search("\[(\w|\s|'|,)+\]", block).group()
    header_word = re.search("\([\s\S]+,", header).group()[1:-1]
    header_pos = re.search(", [\w]+\)", header).group()[2:-1]
    key_tup = (header_word, header_pos)
    body_list = ast.literal_eval(body)
    return (key_tup, body_list)

# synonym_block_parser("(aardvark, noun)\n['edentate', 'farrow', 'anteater', 'ant bear']")

def initialize_graph(filepath):
    word_graph = {}
    with open(filepath, 'r') as myfile:
        data = myfile.read()
    synonym_blocks = re.findall("(\(\w+, \w+\)\n\[(\w|\s|'|,)+\])", data)
    synonym_blocks = map(lambda x : x[0], synonym_blocks)
    block_collector = defaultdict(list)
    # print synonym_blocks
    for block in synonym_blocks:
        tup = synonym_block_parser(block)
        block_collector[tup[0]].append(tup[1])
    for key, value in block_collector.items():
        word_graph[key] = list(OrderedSet(merge_lists(value)))
    return word_graph



# print initialize_graph("C:\\Users\\pgirardet\\Documents\\HackRice\\twenty-questions-thesaurus\\thesaurus_scraper"
#                  "\\thesaurus_scraper\\test_words.txt")
# initialize_graph("C:\\Users\\pgirardet\\Documents\\HackRice\\twenty-questions-thesaurus\\thesaurus_scraper"
#                  "\\thesaurus_scraper\\synonym_list.txt")
