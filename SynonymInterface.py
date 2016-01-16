from enum import Enum
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
    CONJUNCTION= "CONJUNCTION"
    INTERJECTION = "INTERJECTION"


class SynonymInterface:
    """
    The main class for interacting with the word association graph and returning synonym lists to the server.
    """
    # part_of_speech = PartOfSpeech.NOUN
    word_assoc_graph = None

    def __init__(self, part_of_speech):
        if part_of_speech in PartOfSpeech._member_names_:
            self.part_of_speech = PartOfSpeech(part_of_speech)
        else:
            self.part_of_speech = PartOfSpeech("NOUN")
        self.word_assoc_graph = WordGraphParser.initialize_graph("graph_data.json")

    """
    Returns the synonyms of the input word in order of similarity.
    """
    def find_synonyms(self, word):
        return self.word_assoc_graph[word]


