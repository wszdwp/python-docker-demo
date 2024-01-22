import json
import random
from handlers.worddictenum import WordDictType

class WordsUtil:
    wordsDict = dict()
    phraseDict = dict()
    chenyuDict = dict()
    idiomDict = dict()
    
    def __init__(self, wordDictType=WordDictType.XINHUA):
        if wordDictType is WordDictType.XINHUA:
            with open('./data/word.json', 'r') as f:
                data = json.load(f)
                for item in data:
                    self.wordsDict[item['word']] = item
            with open('./data/ci.json', 'r') as f:
                data = json.load(f)
                for item in data:
                    self.phraseDict[item['ci']] = item
        elif wordDictType is WordDictType.XIEHOUYU:
            with open('./data/xiehouyu.json', 'r') as f:
                data = json.load(f)
                self.xiehouyuList = [(d['riddle'], d['answer']) for d in data]
        elif wordDictType is WordDictType.CHENYU:
            with open('./data/idiom.json', 'r') as f:
                data = json.load(f)
                for item in data:
                    self.idiomDict[item['word']] = item
                    self.idiomDict[item['abbreviation']] = item
                
    def searchDefinition(self, word=''):
        definition = None
        if word is None:
            return None
        
        if len(word) < 2:
            wordData = self.searchWord(word)
            if wordData:
                definition = {
                    'word': wordData['word'],
                    'oldword': wordData['oldword'],
                    'strokes': wordData['strokes'],
                    'pinyin': wordData['pinyin'],
                    'radicals': wordData['radicals'],
                    'explanation': wordData['explanation'],
                    'more': wordData['more']
                }
        else:
            wordData = self.searchPhrase(word)
            if wordData:
                definition = {
                    'word': wordData['ci'],
                    'oldword': '',
                    'strokes': '',
                    'pinyin': '',
                    'radicals': '',
                    'explanation': wordData['explanation'],
                    'more': ''
                }
        return definition        
    
    def searchWord(self, word=''):
        if word is None:
            return None
            
        if word in self.wordsDict:
            return self.wordsDict[word]
        return None
    
    def searchPhrase(self, phrase=''):
        if phrase is None:
            return None
        
        if phrase in self.phraseDict:
            return self.phraseDict[phrase]
        return None
    
    def searchIdiom(self, idiom=''):
        if idiom is None:
            return None
        if len(idiom) < 4:
            return None
        
        if idiom in self.idiomDict:
            wordData = self.idiomDict[idiom]
            definition = {
                    'word': wordData['word'],
                    'abbreviation': wordData['abbreviation'],
                    'pinyin': wordData['pinyin'],
                    'explanation': wordData['explanation'],
                    "derivation": wordData['derivation'],
                    "example": wordData['example'],
                }
            return definition 
        return None 
    
    def getNRandomXiehouyu(self, N=10):
        words = set()
        word = ''
        for i in range(0, min(N, 100)):
            while word not in words:           
                pos = random.randint(0, len(self.xiehouyuList)-1)
                word = self.xiehouyuList[pos]
                words.add(word)
            word = ''
        return list(words)

if __name__ == "__main__":
    # wordsUtil = WordsUtil()
    # wordsUtil.searchWord('话')
    # wordsUtil.searchWord('话语')
    wordsUtil = WordsUtil(True)
    print(wordsUtil.getNRandomXiehouyu(5))