from enum import Enum
import json
from WordGraphParser import WordGraphParser


class PartOfSpeech(Enum):
    """
    Enum class for standard parts of speech.
    """
    NOUN = "NOUN"
    PRONOUN = "PRONOUN"
    VERB = "VERB"
    ADJECTIVE = "ADJECTIVE"
    ADVERB = "ADVERB"
    PREPOSITION = "PREPOSITION"
    CONJUNCTION = "CONJUNCTION"
    INTERJECTION = "INTERJECTION"


class SynonymInterface:
    """
    The main class for interacting with the word association graph and returning synonym lists to the server.
    """
    part_of_speech = PartOfSpeech.NOUN
    word_assoc_graph = None

    def __init__(self, part_of_speech):
        if part_of_speech in PartOfSpeech._member_names_:
            self.part_of_speech = PartOfSpeech(part_of_speech)
        else:
            self.part_of_speech = PartOfSpeech("NOUN")
        self.word_assoc_graph = WordGraphParser.initialize_graph("testdata.json")[self.part_of_speech.value]

    """
    Returns the synonyms of the input word in order of similarity.
    """
    def find_synonyms(self, word):
        return self.word_assoc_graph[word]

    def deal_with_synonym_outside_of_graph(self, root, synonym):
        """
        When a synonym outside of the graph is encountered,
        this should be run to find appropriate synonyms for that word.
        :param root: a string key in the graph
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
