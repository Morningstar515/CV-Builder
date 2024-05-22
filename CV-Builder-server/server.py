import mysql.connector
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS, cross_origin
import json
from pdflatex import PDFLaTeX
import subprocess
import os
from flask_cors import CORS
import msql
import re


app = Flask(__name__)
CORS(app)

def returnTemplate(templateName):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute("select Templates from TemplateTable where keyid='jakes' " )

    for i in mycursor:        
        return i
    
test = returnTemplate("jakes")


def compile_latex_to_pdf(latex_file_path):
    # Get the directory containing the LaTeX file
    latex_dir = os.path.dirname(latex_file_path)
    
    # Change directory to the LaTeX file directory
    os.chdir(latex_dir)

    # Compile the LaTeX file using pdflatex
    subprocess.run(['pdflatex', '-interaction=nonstopmode', latex_file_path])
    
    # Get the base name of the LaTeX file (without extension)
    latex_basename = os.path.splitext(os.path.basename(latex_file_path))[0]

    os.chdir("../CV-Builder-server/")
    # Return the path to the generated PDF file
    return os.path.join(latex_dir, f"{latex_basename}.pdf")
    

def open_pdf(pdf_file_path):
    # Check if the PDF file exists
    if os.path.exists(pdf_file_path):
        # Open the PDF file using the default PDF viewer
        subprocess.run(['xdg-open', pdf_file_path])
    else:
        print(f"Error: PDF file '{pdf_file_path}' not found.")

# Example usage:
with open("../CV-Builder-client/ihope.tex", "w") as file:
    # Write your string into the file
    file.write(test[0])

latex_file_path = '../CV-Builder-client/ihope.tex'
pdf_file_path = compile_latex_to_pdf(latex_file_path)

#open_pdf('../CV-Builder-client/ihope.pdf')


# Routes

@app.route("/jakes", methods=['GET'])
def hello():
    return jsonify(test)

@app.route("/testy", methods=['GET'])
def testy():
    print( "<<<<<<<<<<<<<<<<<<<")
    return jsonify({"result": "farts"})


@app.route("/parseName", methods=['POST'])
def parseName():
    key = r"NAME"
    data = request.data.decode("utf-8")
    data = json.loads(data)
    with open("../CV-Builder-client/ihope.tex", "r+") as file:

        for line in file:
            if re.search(key,line):
                print(data["data"])
                print('<<<<<')
                new = re.sub(key, data["data"], line)
                print(new)

    # Compile LaTeX to PDF
    compile_latex_to_pdf(latex_file_path)

    return jsonify({"result": data["data"]})





    

if __name__ =="__main__":
    app.run(port=5000, debug=True)
