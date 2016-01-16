import collections.defaultdict

"""
Class for initializing a word association graph from parsed scraped synonym data.
"""
class WordGraphParser():

    @staticmethod
    def initialize_graph(self, filepath):
        return collections.defaultdict(list)