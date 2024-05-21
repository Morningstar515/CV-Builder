import mysql.connector
from flask import Flask, jsonify;
from flask_cors import CORS, cross_origin
import json
from pdflatex import PDFLaTeX
import subprocess
import os

app = Flask(__name__)
cors = CORS(app, origins='*')



def returnTemplate(templateName):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd='qtip515', database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute("select Templates from TemplateTable where keyid='jakes' " )

    for i in mycursor:        
        return i
    
  
test = returnTemplate("jakes")


def compile_latex_to_pdf(latex_file_path):
    """
    Compile a LaTeX file to PDF using pdflatex.
    
    Args:
        latex_file_path (str): The path to the LaTeX file.
        
    Returns:
        str: The path to the generated PDF file.
    """
    # Get the directory containing the LaTeX file
    latex_dir = os.path.dirname(latex_file_path)
    
    # Change directory to the LaTeX file directory
    os.chdir(latex_dir)
    
    # Compile the LaTeX file using pdflatex
    subprocess.run(['pdflatex', '-interaction=nonstopmode', latex_file_path])
    
    # Get the base name of the LaTeX file (without extension)
    latex_basename = os.path.splitext(os.path.basename(latex_file_path))[0]
    
    # Return the path to the generated PDF file
    return os.path.join(latex_dir, f"{latex_basename}.pdf")
    

def open_pdf(pdf_file_path):
    """
    Open a PDF file using the default PDF viewer.
    
    Args:
        pdf_file_path (str): The path to the PDF file.
    """
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



@app.route("/jakes", methods=['GET'])
def hello():

    latex_content = test
    print(test)

    return json.dumps(test)


@app.route("/parseLatex", methods=['POST'])
def makeLatex():
    print('fart')

latex_file_path = '../CV-Builder-client/ihope.tex'
pdf_file_path = compile_latex_to_pdf(latex_file_path)
open_pdf(pdf_file_path)
    

if __name__ =="__main__":
    app.run(port=5000, debug=True)