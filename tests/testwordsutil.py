import unittest
from handlers.worddictenum import WordDictType
from handlers.wordsutil import WordsUtil

class TestWordsUtil(unittest.TestCase):
    def setUp(self):
        self.xinhuaWordsUtil = WordsUtil(WordDictType.XINHUA)
        self.chenyuWordsUtil = WordsUtil(WordDictType.CHENYU)
        self.xiehouyuWordsUtil = WordsUtil(WordDictType.XIEHOUYU)

    def tearDown(self):
        self.xinhuaWordsUtil = None
        self.chenyuWordsUtil = None
        self.xiehouyuWordsUtil = None
        
    def test_searchWord(self):
        self.assertEqual('话', self.xinhuaWordsUtil.searchWord('话')['word'])
    
    def searchPhrase(self):
        self.assertEqual('话语', self.xinhuaWordsUtil.searchPhrase('话语')['ci'])

if __name__ == '__main__':
    unittest.main()