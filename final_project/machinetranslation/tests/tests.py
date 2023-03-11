import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def testEn2Fr(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Hello'),'Hello')
        self.assertNotEqual(english_to_french('None'),'')
        self.assertNotEqual(english_to_french(0),0)


class TestFrenchToEnglish(unittest.TestCase):
    def testFr2En(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')
        self.assertNotEqual(french_to_english('None'),'')
        self.assertNotEqual(french_to_english(0),0)

if __name__ == '__main__':
    unittest.main()
