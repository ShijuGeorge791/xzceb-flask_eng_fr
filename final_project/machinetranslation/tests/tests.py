import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test 'Hello' gives 'Bonjour'
        self.assertNotEqual(english_to_french('None'), ' ') # test null input

class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test'Bonjour' gives 'Hello'
        self.assertNotEqual(french_to_english('None'), ' ') # test null input

unittest.main()