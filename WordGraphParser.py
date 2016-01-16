import json
import io
from collections import defaultdict

"""
Class for initializing a word association graph from parsed scraped synonym data, returned as a dictionary.
"""


class WordGraphParser:

    def __init__(self):
        pass

    @staticmethod
    def initialize_graph(filepath):
        json_data = io.open(filepath)
        dict_data = json.load(json_data)
        return dict_data
