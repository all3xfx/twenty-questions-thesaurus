from enum import Enum
import WordGraphParser
import json
import WordGraphParser
import cPickle as pickle


# class PartOfSpeech(Enum):
#     """
#     Enum class for standard parts of speech.
#     """
#     NOUN = "noun"
#     PRONOUN = "pronoun"
#     VERB = "verb"
#     ADJECTIVE = "adjective"
#     ADVERB = "adverb"
#     PREPOSITION = "preposition"
#     CONJUNCTION = "conjunction"
#     INTERJECTION = "interjection"


class SynonymInterface:
    """
    The main class for interacting with the word association graph and returning synonym lists to the server.
    """
    part_of_speech = "noun"
    word_assoc_graph = None

    def __init__(self, part_of_speech):
        self.part_of_speech = part_of_speech
        # if part_of_speech in PartOfSpeech._member_names_:
        #     self.part_of_speech = PartOfSpeech(part_of_speech)
        # else:
        #     self.part_of_speech = PartOfSpeech("NOUN")
        # with open('synonym_graph.pkl', 'rb') as input:
        #     graph = pickle.load(input)
        #     self.word_assoc_graph = graph
        #     print "Synonym graph successfully loaded."
        self.word_assoc_graph = WordGraphParser.initialize_graph("thesaurus_scraper/thesaurus_scraper/synonym_list.txt")

    """
    Returns the synonyms of the input word in order of similarity.
    """
    def find_synonyms(self, word):
        return self.word_assoc_graph[(word, self.part_of_speech)]

    def deal_with_synonym_outside_of_graph(self, root, synonym):
        """
        When a synonym outside of the graph is encountered,
        this should be run to find appropriate synonyms for that word.
        :param root: a tuple key in the graph
        :param synonym: a string key not in the graph
        :return: a dict of string: list(string) showing the proper synonyms
        """
        close_synonyms = list(self.word_assoc_graph[root])
        close_synonyms.remove(synonym)
        output_synonyms = [root]
        for syn in close_synonyms:
            if synonym in self.word_assoc_graph[syn]:
                output_synonyms.append(syn)
        return {synonym: output_synonyms}
