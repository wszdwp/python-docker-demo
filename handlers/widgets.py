import mysql.connector
import json

class Widgets:
    
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="mysqldb",
            user="root",
            password="p@ssw0rd1",
            database="inventory"
        )
        cursor = self.mydb.cursor()
        cursor.execute("DROP DATABASE IF EXISTS inventory")
        cursor.execute("CREATE DATABASE inventory")
        cursor.execute("DROP TABLE IF EXISTS widgets")
        cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
        cursor.close()
        
    def read(self, query='SELECT * FROM widgets'):
        cursor = self.mydb.cursor()
        cursor.execute(query)

        row_headers=[x[0] for x in cursor.description] #this will extract row headers

        results = cursor.fetchall()
        json_data=[]
        for result in results:
            json_data.append(dict(zip(row_headers,result)))
        cursor.close()
        
        return json.dumps(json_data)