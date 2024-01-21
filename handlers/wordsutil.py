import json
import random

class WordsUtil:
    wordsDict = dict()
    phraseDict = dict()
    xiehouyuDict = dict()
    
    def __init__(self, xiehouyu=False):
        if not xiehouyu:
            with open('./data/word.json', 'r') as f:
                data = json.load(f)
                for item in data:
                    self.wordsDict[item['word']] = item
            with open('./data/ci.json', 'r') as f:
                data = json.load(f)
                for item in data:
                    self.phraseDict[item['ci']] = item
        else:
            with open('./data/xiehouyu.json', 'r') as f:
                data = json.load(f)
                self.xiehouyuList = [(d['riddle'], d['answer']) for d in data]
                
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
    
    def getNRandomXiehouyu(self, N=10):
        words = set()
        word = ''
        for i in range(0, min(N, 100)):
            while word not in words:           
                pos = random.randint(0, len(self.xiehouyuList)-1)
                word = self.xiehouyuList[pos]
                print('pos ' + str(pos) + ' word: ' + str(word))
                words.add(word)
            word = ''
        return list(words)

if __name__ == "__main__":
    # wordsUtil = WordsUtil()
    # wordsUtil.searchWord('话')
    # wordsUtil.searchWord('话语')
    wordsUtil = WordsUtil(True)
    print(wordsUtil.getNRandomXiehouyu(5))