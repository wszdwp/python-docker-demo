import os
from flask import Flask, request
from flask import render_template
from flask import send_from_directory
from config import TestingConfig, Config
from handlers.price import Price
from handlers.widgets import Widgets
from handlers.worddictenum import WordDictType
from handlers.wordsutil import WordsUtil
from handlers.fileutil import FileUtil
from handlers.pdfocr import PdfOcr

app = Flask(__name__)
app.config.from_object(TestingConfig())
app.logger.info('App config: %s', app.config)

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
    
@app.route('/chenyujielong', methods=['GET', 'POST'])
def chenyujielong():
    if request.method == 'GET':
        return render_template('chenyujielong.html')
    elif request.method == 'POST':
        word = request.form['word'].strip()
        number = request.form['number'].strip()
        answers = request.form.getlist('answers')
        wordsUtil = WordsUtil(WordDictType.CHENYU)
        if number.isdigit():
            idioms = wordsUtil.findNextNIdioms(word, int(number))
            if answers:
                allIdioms = wordsUtil.findNextAllIdioms(word, int(number))
                return render_template('chenyujielong.html', idioms=idioms, number=number, count=len(idioms), allIdioms=allIdioms)
            else:
                return render_template('chenyujielong.html', idioms=idioms, number=number, count=len(idioms))
        else:
            return render_template('chenyujielong.html', idioms=None, msg='Invalid input')
    
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
        
@app.route('/ocr', methods=['GET', 'POST'])
def ocr():
    if request.method == 'GET':
        return render_template('ocrtool.html')
    elif request.method == 'POST':
        if 'file' not in request.files:
            return render_template('ocrtool.html', msg='no such file')
        file = request.files['file']
        fileUtil = FileUtil(app.config['UPLOAD_FOLDER'], app.config['ALLOWED_EXTENSIONS'])
        sourceFilePath = fileUtil.saveFile(file)
        app.logger.info('saved file into: %s', sourceFilePath)
        pdfocr = PdfOcr()
        outputFilePath = pdfocr.ocrFile(sourceFilePath, file.filename)
        return render_template('ocrtool.html', sourceFilePath=sourceFilePath, outputFilePath=outputFilePath)
    
@app.route('/uploads/<fileName>', methods=['GET'])
def uploads(fileName):
    uploadPath = app.config['UPLOAD_FOLDER']
    fullPath = os.path.join(uploadPath, fileName)
    with open(fullPath, 'rb') as f:
        return send_from_directory(uploadPath, fileName)
    
@app.route('/output/<fileName>', methods=['GET'])
def output(fileName):
    outputPath = app.config['OUTPUT_FOLDER']
    fullPath = os.path.join(outputPath, fileName)
    with open(fullPath, 'rb') as f:
        return send_from_directory(outputPath, fileName)

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
