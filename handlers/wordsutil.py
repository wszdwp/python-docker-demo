import json
import random
from handlers.worddictenum import WordDictType

class WordsUtil:
    wordsDict = dict()
    phraseDict = dict()
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
            self.idiomsListDict = dict()
            with open('./data/idiom.json', 'r') as f:
                data = json.load(f)
                for item in data:
                    self.idiomDict[item['word']] = item
                    self.idiomDict[item['abbreviation']] = item
                    firstPinyin = item['pinyin'].split(' ')[0]
                    if firstPinyin not in self.idiomsListDict:
                        self.idiomsListDict[firstPinyin] = list()
                    self.idiomsListDict[firstPinyin].append(item)
                
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
    
    def findNextNIdioms(self, idiom='', N=1):
        idiomEntity = self.searchIdiom(idiom)
        if idiomEntity is None:
            return [idiom]
        
        idioms = [idiomEntity]
        idiomWords = set()
        idiomWords.add(idiomEntity['word'])
        next = ''
        for i in range(1, min(N, 100)):
            candidatesSize = 0
            j = 0
            while next not in idiomWords:
                lastPinyin = idiomEntity['pinyin'].split(' ')[-1]
                candidatesSize = len(self.idiomsListDict[lastPinyin])
                if j >= candidatesSize:
                    break
                next = self.idiomsListDict[lastPinyin][j]['word']
                if next not in idiomWords:
                    break
                j = j + 1
            # Break if cannot find more idioms
            if len(next) == 0 or j >= candidatesSize or next in idiomWords:
                break
            idiomWords.add(next)
            idiom = next
            idiomEntity = self.searchIdiom(idiom)
            idioms.append(idiomEntity)
            next = ''
        return list(idioms)
        
    def findNextAllIdioms(self, idiom='', N=1):
        allIdioms = []
        idiomEntity = self.searchIdiom(idiom)            
        if idiomEntity is None:
            idioms = [idiom]
            allIdioms.append(idioms)
            return allIdioms
        
        while idiomEntity:        
            print('pinyin: ' + idiomEntity['pinyin'])
            lastPinyin = idiomEntity['pinyin'].split(' ')[-1]
            if lastPinyin not in self.idiomsListDict:
                break
            nextIdioms = self.idiomsListDict[lastPinyin]
            allIdioms.append(nextIdioms)
            # idiomEntity = nextIdioms[0]
            N = N - 1
            if N == 0:
                break
            idiomEntity = nextIdioms[random.randint(0, len(nextIdioms)-1)]
        return allIdioms
    
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
    wordsUtil = WordsUtil(WordDictType.XINHUA)
    print(wordsUtil.searchWord('话'))
    print(wordsUtil.searchWord('话语'))
    wordsUtil = WordsUtil(WordDictType.XIEHOUYU)
    print(wordsUtil.getNRandomXiehouyu(5))