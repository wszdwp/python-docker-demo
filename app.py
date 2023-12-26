import mysql.connector
import json
from flask import Flask, request
from price import Price
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404

@app.route('/pricelist', methods=['GET', 'POST'])
def food_price():
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
def get_widgets():
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
def db_init():
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
