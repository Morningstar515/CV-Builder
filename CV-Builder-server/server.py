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



def returnTemplate(templateName):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()
   # mycursor.execute("select Templates from TemplateTable where keyid='jakes' " )
    mycursor.execute("select BaseTex from JakesTable")


    for i in mycursor:     
        with open("../CV-Builder-client/ihope.tex", "w") as file:
            # Write your string into the file
            file.write(i[0])
        file.close()

    compile_latex_to_pdf("../CV-Builder-client/ihope.tex")

test = returnTemplate("jakes")
  

def open_pdf(pdf_file_path):
    # Check if the PDF file exists
    if os.path.exists(pdf_file_path):
        # Open the PDF file using the default PDF viewer
        subprocess.run(['xdg-open', pdf_file_path])
    else:
        print(f"Error: PDF file '{pdf_file_path}' not found.")


# Original Compile
latex_file_path = '../CV-Builder-client/ihope.tex'
pdf_file_path = compile_latex_to_pdf(latex_file_path)


# Routes
@app.route("/jakes", methods=['GET'])
def restart():
    returnTemplate('jakes')
    return jsonify({"result": "farts"})

@app.route("/testy", methods=['GET'])
def testy():
    return jsonify({"result": "farts"})




@app.route("/addEducation", methods=['GET'])
def addEducationHeader():

    # Read file till insertion point found and end of document     
    with open("../CV-Builder-client/ihope.tex", "r") as file:
        content = file.readlines()
        index = 0
        for line in content:
            if "\end{document}" in line:
                break;
            index += 1

        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.tex", "w") as file:
            writeLine = 0
            for line in content:
                if writeLine == index:
                    file.write('\section{Education}' + '\n' + '\\resumeSubHeadingListStart' + '\n' + '\n' + '\\resumeSubHeadingListEnd' + '\n')

                # Write your string into the file
                file.write(line)
                writeLine += 1
        file.close()
    file.close()
    compile_latex_to_pdf(latex_file_path)
    return jsonify({"message":"success"})



@app.route("/parseBasics", methods=['POST'])
def parseBasics():
    data = request.data.decode("utf-8")
    data = json.loads(data)

    # Pull section from DB
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute("select Header from JakesTable")

    for i in mycursor:
        # Read file till insertion point found and end of document     
        with open("../CV-Builder-client/ihope.tex", "r") as file:
            content = file.readlines()
            index = 0
            for line in content:
                if "\end{document}" in line:
                    break;
                index += 1

            # Rewrite to file and insert new section at 'index' from previous loop
            with open("../CV-Builder-client/ihope.tex", "w") as file:
                writeLine = 0
                for line in content:
                    if writeLine == index:
                        file.write(i[0] + '\n')

                    # Write your string into the file
                    file.write(line)
                    writeLine += 1



    for key in data:
        newline = ""
        oldLine = ""
        with open("../CV-Builder-client/ihope.tex", "r+") as file:
            for line in file:
                if re.search(key,line):
                    oldLine = line
                    newline = re.sub(key, data[key], line)
                    break;
                    #line.replace(line,newline)
        if oldLine:    
            with open("../CV-Builder-client/ihope.tex", "r+") as file:
                lines = file.readlines()

                for i, line in enumerate(lines):
                    if line.strip() == oldLine.strip():
                        lines[i] = newline

                file.seek(0)
                file.truncate()
                file.writelines(lines) 
            
            with open("../CV-Builder-client/ihope.tex", "r") as file:
                for line in file:
                    print(line)

        # Compile LaTeX to PDF
        compile_latex_to_pdf(latex_file_path)
        return jsonify({"result": ""})


@app.route("/parseEducation", methods=['POST'])
def parseEducation():
    data = request.json

    # Pull section from DB
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute("select School from JakesTable")

    for i in mycursor:
        
        #Replacing ending number this correct entry number
        mod = i[0].replace('1',str(data["count"][0]))
        tup = (mod,)
        i = tup

        # Read file till insertion point found and end of document     
        with open("../CV-Builder-client/ihope.tex", "r") as file:
            content = file.readlines()
            
            pastLocationMarker = False  #To account for latex headers with the same name, this allows us to not insert unless we have passed the marker for a certain section
            index = 0
            for line in content:
                if "\\section{Education}" in line:
                    pastLocationMarker = True

                if "\\resumeSubHeadingListEnd" in line and pastLocationMarker:
                    break;
                index += 1

            # Rewrite to file and insert new section at 'index' from previous loop
            with open("../CV-Builder-client/ihope.tex", "w") as file:
                writeLine = 0
                for line in content:
                    if writeLine == index:
                        file.write(i[0] + '\n')

                    # Write your string into the file
                    file.write(line)
                    writeLine += 1
            file.close()
        file.close()

    for key in data:

        newline = ""
        oldLine = ""
        with open("../CV-Builder-client/ihope.tex", "r+") as file:
            for line in file:

                if re.search(key,line):
                    oldLine = line
                    newline = re.sub(key, data[key], line)
                    line.replace(line,newline)
        file.close()

        with open("../CV-Builder-client/ihope.tex", "r+") as file:
            lines = file.readlines()  
            for i, line in enumerate(lines):
                if line.strip() == oldLine.strip():
                    lines[i] = newline

            file.seek(0)
            file.writelines(lines)
        file.close()

        
    # Compile LaTeX to PDF
    compile_latex_to_pdf(latex_file_path)

    return jsonify({"message": "success",
                    "data": "data"})



@app.route("/parseExperience", methods=['POST'])
def parseExperience():
    data = request.json

    # data = request.data.decode("utf-8")
    # data = json.loads(data)

    for key in data:

        newline = ""
        oldLine = ""
        with open("../CV-Builder-client/ihope.tex", "r+") as file:
            for line in file:
                if re.search(key,line):
                    oldLine = line
                    newline = re.sub(key, data[key], line)
                    line.replace(line,newline)
        file.close()

        with open("../CV-Builder-client/ihope.tex", "r+") as file:
            lines = file.readlines()  # Read all lines into a list

            for i, line in enumerate(lines):
                if line.strip() == oldLine.strip():
                    lines[i] = newline # Replace the old line with newline

            file.seek(0)  # Move the file pointer to the beginning
            file.writelines(lines)  # Write the modified lines back to the file
        file.close()
        

    # Compile LaTeX to PDF
    compile_latex_to_pdf(latex_file_path)

    return jsonify({"message": "success"})

    

if __name__ =="__main__":
    app.run(port=5000, debug=True)
