import mysql.connector
import json
from flask import Flask, request
from price import Price
from flask import render_template
from wordsutil import WordsUtil

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
        print("get")
        return render_template('xinhuadict.html')
    elif request.method == 'POST':
        print("post")
        word = request.form['word']
        wordsUtil = WordsUtil()
        wordData = wordsUtil.searchWord(word)
        data = '没找到！'
        if wordData:
            data = {
                'word': wordData['word'],
                'oldword': wordData['oldword'],
                'strokes': wordData['strokes'],
                'pinyin': wordData['pinyin'],
                'radicals': wordData['radicals'],
                'explanation': wordData['explanation'],
                'more': wordData['more']
            }
        return render_template('xinhuadict.html', word=word, definition=data)

@app.route('/pricelist', methods=['GET', 'POST'])
def pricelist():
    if request.method == 'GET':
        return render_template('foodprice.html')
    elif request.method == 'POST':
        craftName = request.form['craftname']
        markets = request.form['markets']
        requestJson = {
            'craftIndex': 13235,
            'craftName': craftName,
            'eudName': markets,
            'queryDateType': 0,
            'pageNo': 1
        }
        return get_price(requestJson)

def get_price(requestJson):
    price = Price()
    res = price.getPrice(requestJson)
    return res.json()

@app.route('/widgets')
def widgets():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="inventory"
    )
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM widgets")

    row_headers=[x[0] for x in cursor.description] #this will extract row headers

    results = cursor.fetchall()
    json_data=[]
    for result in results:
        json_data.append(dict(zip(row_headers,result)))

    cursor.close()

    return json.dumps(json_data)

@app.route('/initdb')
def initdb():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS inventory")
    cursor.execute("CREATE DATABASE inventory")
    cursor.close()

    mydb = mysql.connector.connect(
        host="mysqldb",
        user="root",
        password="p@ssw0rd1",
        database="inventory"
    )
    cursor = mydb.cursor()

    cursor.execute("DROP TABLE IF EXISTS widgets")
    cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
    cursor.close()

    return 'init database'

if __name__ == "__main__":
    app.run(host ='0.0.0.0')
