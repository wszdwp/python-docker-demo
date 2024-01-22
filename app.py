from flask import Flask, request
from flask import render_template
from handlers.price import Price
from handlers.widgets import Widgets
from handlers.worddictenum import WordDictType
from handlers.wordsutil import WordsUtil

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    elif request.method == 'POST':
        name = request.form['name']
        return render_template('home.html', name=name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404

@app.route('/xinhuadict', methods=['GET', 'POST'])
def xinhuadict():
    if request.method == 'GET':
        return render_template('xinhuadict.html')
    elif request.method == 'POST':
        word = request.form['word'].strip()
        wordsUtil = WordsUtil(WordDictType.XINHUA)
        definition = wordsUtil.searchDefinition(word)
        return render_template('xinhuadict.html', word=word, definition=definition)

@app.route('/chenyudict', methods=['GET', 'POST'])
def chenyudict():
    if request.method == 'GET':
        return render_template('chenyudict.html')
    elif request.method == 'POST':
        word = request.form['word'].strip()
        wordsUtil = WordsUtil(WordDictType.CHENYU)
        definition = wordsUtil.searchIdiom(word)
        return render_template('chenyudict.html', word=word, definition=definition)
    
@app.route('/xiehouyu', methods=['GET', 'POST'])
def xiehouyu():
    if request.method == 'GET':
        return render_template('xiehouyu.html')
    elif request.method == 'POST':
        wordsUtil = WordsUtil(WordDictType.XIEHOUYU)
        number = request.form['number'].strip()
        if number.isdigit():
            words = wordsUtil.getNRandomXiehouyu(int(number))
            return render_template('xiehouyu.html', words=words, number=number)
        else:
            return render_template('xiehouyu.html', words=None, msg='Invalid input')

@app.route('/pricelist', methods=['GET', 'POST'])
def pricelist():
    if request.method == 'GET':
        return render_template('foodprice.html')
    elif request.method == 'POST':
        craftName = request.form['craftname'].strip()
        markets = request.form['markets']
        requestJson = {
            'craftIndex': 13235,
            'craftName': craftName,
            'eudName': markets,
            'queryDateType': 0,
            'pageNo': 1
        }
        price = Price()
        res = price.getPrice(requestJson)
        return res

@app.route('/widgets')
def widgets():
    widgets = Widgets()
    return widgets.read()


if __name__ == "__main__":
    app.run(host ='0.0.0.0')
