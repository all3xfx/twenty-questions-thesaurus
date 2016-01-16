from unittest import TestCase
from SynonymInterface import SynonymInterface
from SynonymInterface import PartOfSpeech


class TestSynonymInterface(TestCase):
    word_assoc_graph = {"red" : ["orange", "yellow", "crimson"], "orange" : ["yellow", "red", "crimson"], "yellow" : ["orange", "red"]}
    test_interface = SynonymInterface("NOUN")
    test_interface.word_assoc_graph = word_assoc_graph

    def test_initialization(self):
        default_pos_interface = SynonymInterface("this shouldn't be valid")
        noun_pos_interface = SynonymInterface("NOUN")
        verb_pos_interface = SynonymInterface("VERB")
        self.assertEqual(default_pos_interface.part_of_speech, PartOfSpeech.NOUN)
        self.assertEqual(noun_pos_interface.part_of_speech, PartOfSpeech.NOUN)
        self.assertEqual(verb_pos_interface.part_of_speech, PartOfSpeech.VERB)

    def test_find_synonyms(self):
        self.assertEquals(self.test_interface.find_synonyms("yellow"), ["orange", "red"])
        self.assertEquals(self.test_interface.find_synonyms("red"), ["orange", "yellow", "crimson"])

    def test_unknown_finder(self):
        crimson_dict = self.test_interface.deal_with_synonym_outside_of_graph("red", "crimson")
        self.assertEqual(crimson_dict["crimson"], ["red", "orange"])
