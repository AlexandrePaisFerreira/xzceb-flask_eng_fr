import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def testEn2Fr(self):
        self.assertEqual(englishToFrench('Hello'),'Bonjour')
        self.assertNotEqual(englishToFrench('Hello'),'Hello')
        self.assertNotEqual(englishToFrench('None'),'')
        self.assertNotEqual(englishToFrench(0),0)


class TestFrenchToEnglish(unittest.TestCase):
    def testFr2En(self):
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')
        self.assertNotEqual(frenchToEnglish('Bonjour'),'Bonjour')
        self.assertNotEqual(frenchToEnglish('None'),'')
        self.assertNotEqual(frenchToEnglish(0),0)

if __name__ == '__main__':
    unittest.main()