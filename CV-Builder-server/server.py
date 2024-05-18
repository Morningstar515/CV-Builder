import mysql.connector
from flask import Flask, jsonify;
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/hello", methods=['GET'])
def hello():
    return jsonify(
        {
            "hellos": [
                'hi',
                'hola'
            ]
        }
    )

def returnTemplate(templateName):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd='qtip515', database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute("select Templates from TemplateTable where keyid={templateName}")
    for i in mycursor:
        return i
    

if __name__ =="__main__":
    app.run(port=5000, debug=True)