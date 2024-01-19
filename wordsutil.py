import json

class WordsUtil:
    wordsDict = dict()
    
    def __init__(self):
        with open('./data/word.json', 'r') as f:
            data = json.load(f)
            for item in data:
                self.wordsDict[item['word']] = item

    def searchWord(self, word=''):
        if word is None:
            return None
        
        if word in self.wordsDict:
            return self.wordsDict[word]
        return None

if __name__ == "__main__":
    wordsUtil = WordsUtil()
    wordsUtil.searchWord('话')