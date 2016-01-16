from enum import Enum


"""
Enum class for standard parts of speech.
"""
class PartOfSpeech(Enum):
    noun = "noun"
    pronoun = "pronoun"
    verb = "verb"
    adjective = "adjective"
    adverb = "adverb"
    preposition = "preposition"
    conjunction = "conjunction"
    interjection = "interjection"



"""
The main class for interacting with the word association graph and returning synonym lists to the server.
"""
class SynonymInterface:
    part_of_speech = PartOfSpeech.noun
    word_assoc_graph = None

    def __init__(self, part_of_speech):
        if part_of_speech in PartOfSpeech._member_names_:
            self.part_of_speech = PartOfSpeech(part_of_speech)
        else:
            self.part_of_speech = PartOfSpeech("noun")

    """
    Returns the synonyms of the input word in order of similarity.
    """
    def find_synonyms(self, word):
        return self.word_assoc_graph[word]


