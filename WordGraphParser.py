from collections import defaultdict

"""
Class for initializing a word association graph from parsed scraped synonym data, returned as a dictionary.
"""
class WordGraphParser():

    @staticmethod
    def initialize_graph(filepath):
        return defaultdict(list)