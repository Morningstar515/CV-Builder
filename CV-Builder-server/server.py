import mysql.connector
from flask import Flask, jsonify;
from flask_cors import CORS, cross_origin
import json
from pdflatex import PDFLaTeX
import subprocess


app = Flask(__name__)
cors = CORS(app, origins='*')



def returnTemplate(templateName):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd='qtip515', database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute("select Templates from TemplateTable where keyid='jakes'")
    for i in mycursor:
        f = open("latex.html", "a")
        p = json.dumps(i)
        f.write(p)
        
        return i
    
    


test = returnTemplate("jakes")
test = test[0]


@app.route("/jakes", methods=['GET'])
def hello():

    latex_content = test
    print(test)

    formatted_content = format_latex(latex_content)

    filename = 'output.tex'
    generate_latex_file(formatted_content, filename)

    # pdfl = PDFLaTeX.from_texfile('output.tex')
    # pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=True)

    return json.dumps(test)


@app.route("/parseLatex", methods=['POST'])
def makeLatex():
    print('fart')


def format_latex(latex_code):
    formatted_code = latex_code.strip()
    formatted_code = formatted_code.replace('\n', ' \n')  # Add space before newline
    formatted_code = formatted_code.replace('end{tabular*', '\\end{tabular*}')  # Fix tabular* end tag
    formatted_code = formatted_code.replace('section{', '\\section{')  # Fix section tag
    formatted_code = formatted_code.replace('item', '\\item')  # Fix item tag
    formatted_code = formatted_code.replace('emph{', '\\emph{')  # Fix emph tag
    formatted_code = formatted_code.replace('small', '\\small')  # Fix small tag
    formatted_code = formatted_code.replace('documentclass[', '\\documentclass[')  # Fix documentclass tag
    formatted_code = formatted_code.replace('renewcommand', '\\renewcommand')  # Fix renewcommand tag
    formatted_code = formatted_code.replace('usepackage', '\\usepackage')  # Fix usepackage tag
    return formatted_code







def generate_latex_file(latex_string, filename):
    with open(filename, 'w') as f:
        f.write(latex_string)
    print(f"LaTeX file '{filename}' generated successfully.")


def format_latex_content(content):
    # Split the content by section delimiter
    sections = content.split('\n%-----------')
    
    # Join each section with a newline and return
    return '\n\n'.join(sections)




def compile_tex(tex_file):
    subprocess.run(['pdflatex', tex_file])
    subprocess.run(['pdflatex', tex_file])  # Run twice to resolve references
    subprocess.run(['pdflatex', tex_file])  # Run thrice to ensure table of contents updates
    subprocess.run(['xdg-open', tex_file.replace('.tex', '.pdf')])  # Open PDF file



if __name__ == "__main__":
    tex_file = "output.tex"  # Replace with your .tex file name
    compile_tex(tex_file)



    

if __name__ =="__main__":
    app.run(port=5000, debug=True)