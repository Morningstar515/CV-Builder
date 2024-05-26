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
import time


app = Flask(__name__)
CORS(app)
currIndex = 0

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


def compileText():
    with open('../CV-Builder-client/ihope.txt', 'r') as txt_file:
        content = txt_file.read()

    with open('../CV-Builder-client/ihope.tex', 'w') as tex_file:
            tex_file.write(content)




def returnTemplate(templateName):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()
   # mycursor.execute("select Templates from TemplateTable where keyid='jakes' " )
    mycursor.execute("select BaseTex from JakesTable")


    for i in mycursor:     
        with open("../CV-Builder-client/ihope.txt", "w") as file:
            # Write your string into the file
            file.write(i[0])
    compileText()
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

def replace_capitalized_words(file_path, replacements):

    with open(file_path, 'r') as file:
        content = file.read()
    def replacer(match):
        word = match.group(0)
        return replacements.get(word, word)

    modified_content = re.sub(r'\b[A-Z][A-Z0-9]*\b', replacer, content)

    with open(file_path, 'w') as file:
        file.write(modified_content)




@app.route("/addEducation", methods=['GET'])
def addEducationHeader():

    # Read file till insertion point found and end of document     
    with open("../CV-Builder-client/ihope.txt", "r") as file:
        content = file.readlines()
        index = 0
        for line in content:
            if "\end{document}" in line:
                break;
            index += 1

        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            writeLine = 0
            for line in content:
                if writeLine == index:
                    file.write('\section{Education}' + '\n' + '\\resumeSubHeadingListStart' + '\n' + '\n' + '\\resumeSubHeadingListEnd' + '\n')
                # Write your string into the file
                file.write(line)
                writeLine += 1
    compileText()
    compile_latex_to_pdf(latex_file_path)
    return jsonify({"message":"success"})


@app.route("/addExperience", methods=['GET'])
def addExperienceHeader():

    # Read file till insertion point found and end of document     
    with open("../CV-Builder-client/ihope.txt", "r+") as file:
        content = file.readlines()
        index = 0
        for line in content:
            if "\end{document}" in line:
                break;
            index += 1

        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            writeLine = 0
            for line in content:
                if writeLine == index:
                    file.write('\section{Experience}' + '\n' + '\\resumeSubHeadingListStart' + '\n' + '\n' + '\\resumeSubHeadingListEnd' + '\n')

                # Write your string into the file
                file.write(line)
                writeLine += 1
            
    compileText()
    compile_latex_to_pdf(latex_file_path)
    return jsonify({"message":"success"})



@app.route("/addProjects", methods=['GET'])
def addProjectsHeader():

    # Read file till insertion point found and end of document     
    with open("../CV-Builder-client/ihope.txt", "r") as file:
        content = file.readlines()
        index = 0
        for line in content:
            if "\end{document}" in line:
                break;
            index += 1

        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            writeLine = 0
            for line in content:
                if writeLine == index:
                    file.write('\section{Projects}' + '\n' + '\\resumeSubHeadingListStart' + '\n' + '\n' + '\\resumeSubHeadingListEnd' + '\n')
                # Write your string into the file
                file.write(line)
                writeLine += 1
    compileText()
    compile_latex_to_pdf(latex_file_path)
    return jsonify({"message":"success"})


@app.route("/addSkills", methods=['GET'])
def addSkillsHeader():

    # Read file till insertion point found and end of document     
    with open("../CV-Builder-client/ihope.txt", "r") as file:
        content = file.readlines()
        index = 0
        for line in content:
            if "\end{document}" in line:
                break;
            index += 1

        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            writeLine = 0
            for line in content:
                if writeLine == index:
                    file.write('\section{Technical Skills}' + '\n' +  "\\begin{itemize}[leftmargin=0.15in, label={}]" + '\n' + '\n' + '\\end{itemize}' + '\n')
                # Write your string into the file
                file.write(line)
                writeLine += 1
    compileText()
    compile_latex_to_pdf(latex_file_path)
    return jsonify({"message":"success"})


##########################################################################################################


## Basics
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
        with open("../CV-Builder-client/ihope.txt", "r") as file:
            content = file.readlines()
            index = 0
            for line in content:
                if "\end{document}" in line:
                    break;
                index += 1

            # Rewrite to file and insert new section at 'index' from previous loop
            with open("../CV-Builder-client/ihope.txt", "r+") as file:
                writeLine = 0
                for line in content:
                    if writeLine == index:
                        file.write(i[0] + '\n')

                    # Write your string into the file
                    file.write(line)
                    writeLine += 1

    replace_capitalized_words("../CV-Builder-client/ihope.txt", data)
        
    compileText()
    # Compile LaTeX to PDF
    compile_latex_to_pdf(latex_file_path)

    return jsonify({"result": ""})

##############################################################################################################

## Education
@app.route("/parseEducation", methods=['POST'])
def parseEducation():
    data = request.json
    print(data)
    print('<<<<')

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
        with open("../CV-Builder-client/ihope.txt", "r") as file:
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
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            writeLine = 0
            for line in content:
                if writeLine == index:
                    file.write(i[0] + '\n')

                # Write your string into the file
                file.write(line)
                writeLine += 1
                

    replace_capitalized_words("../CV-Builder-client/ihope.txt", data)
    compileText()
        # Compile LaTeX to PDF
    compile_latex_to_pdf(latex_file_path)

    return jsonify({"message": "success",
                    "data": "data"})

###########################################################################################################

## Experience
@app.route("/parseExperience", methods=['POST'])
def parseExperience():
    data = request.json
    # Pull section from DB
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute("select Experience from JakesTable")

    for i in mycursor:
        
        #Replacing ending number this correct entry number
        mod = i[0].replace('1',str(data["count"][0]))
        tup = (mod,)
        i = tup

        # Read file till insertion point found and end of document     
        with open("../CV-Builder-client/ihope.txt", "r") as file:
            content = file.readlines()
            
            pastLocationMarker = False  #To account for latex headers with the same name, this allows us to not insert unless we have passed the marker for a certain section
            index = 0
            for line in content:
                if "\\section{Experience}" in line:
                    pastLocationMarker = True

                if "\\resumeSubHeadingListEnd" in line and pastLocationMarker:
                    break;
                index += 1

            
        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            writeLine = 0
            for line in content:
                if writeLine == index:
                    file.write(i[0] + '\n')

                # Write your string into the file
                file.write(line)
                writeLine += 1

    #Append the new data
    with open("../CV-Builder-client/ihope.txt", "r+") as file:
        content = file.readlines()    

        for key in data:
            if key == 'count':
                continue
            
            for i in range (len(content)):

                if re.search(key,content[i]):
                    oldLine = content[i]
                    new = re.sub(key,data[key],oldLine)
                    content[i] = new
       
        file.seek(index)
        for line in content:
            file.write(line)
            
    replace_capitalized_words("../CV-Builder-client/ihope.txt", data)
    compileText()
    # Compile LaTeX to PDF
    compile_latex_to_pdf(latex_file_path)
    return jsonify({"message": "success"})

###########################################################################################################

# Projects
@app.route("/parseProjects", methods=['POST'])
def parseProjects():
    data = request.json

    # Pull section from DB
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute("select Projects from JakesTable")

    for i in mycursor:
        
        #Replacing ending number this correct entry number
        mod = i[0].replace('1',str(data["count"][0]))
        tup = (mod,)
        i = tup

        # Read file till insertion point found and end of document     
        with open("../CV-Builder-client/ihope.txt", "r") as file:
            content = file.readlines()
            
            #To account for latex headers with the same name, this allows us to not insert unless we have passed 
            #the marker for a certain section         
            pastLocationMarker = False  
            index = 0
            for line in content:
                if "\\section{Projects}" in line:
                    pastLocationMarker = True

                if "\\resumeSubHeadingListEnd" in line and pastLocationMarker:
                    break;
                index += 1

            
        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            writeLine = 0
            for line in content:
                if writeLine == index:
                    file.write(i[0] + '\n')

                # Write your string into the file
                file.write(line)
                writeLine += 1

    #Append the new data
    with open("../CV-Builder-client/ihope.txt", "r+") as file:
        content = file.readlines()    
        for key in data:
            if key == 'count':
                continue
            
            for i in range (len(content)):

                if re.search(key,content[i]):
                    oldLine = content[i]
                    new = re.sub(key,data[key],oldLine)
                    content[i] = new
       
        file.seek(index)
        for line in content:
            file.write(line)
            
    replace_capitalized_words("../CV-Builder-client/ihope.txt", data)
    compileText()
    # Compile LaTeX to PDF
    compile_latex_to_pdf(latex_file_path)
    return jsonify({"message": "success"})


###########################################################################################################

# Skills
@app.route("/parseSkills", methods=['POST'])
def parseSkills():
    data = request.json
    print(data)
    print('<<<<<!!')

    # Pull section from DB
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute("select Skills from JakesTable")

    for i in mycursor:
        
        #Replacing ending number this correct entry number
        mod = i[0].replace('1',str(data["count"][0]))
        tup = (mod,)
        i = tup

        # Read file till insertion point found and end of document     
        with open("../CV-Builder-client/ihope.txt", "r") as file:
            content = file.readlines()
            
            #To account for latex headers with the same name, this allows us to not insert unless we have passed 
            #the marker for a certain section         
            pastLocationMarker = False  
            index = 0
            for line in content:
                if "\\section{Technical Skills}" in line:
                    pastLocationMarker = True

                if "\\end{itemize}" in line and pastLocationMarker:
                    break;
                index += 1

            
        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            writeLine = 0
            for line in content:
                print(writeLine)
                print(index)
                if writeLine == index:
                    print(i[0])
                    file.write(i[0] + '\n')

                    print('????')
                    print('????')
                    print('????')
                # Write your string into the file
                file.write(line)
                writeLine += 1

    #Append the new data
    with open("../CV-Builder-client/ihope.txt", "r+") as file:
        content = file.readlines()    
        print(data)
        print('<<<<')
        for key in data:
            if key == 'count':
                continue
            
            for i in range (len(content)):

                if re.search(key,content[i]):
                    oldLine = content[i]
                    new = re.sub(key,data[key],oldLine)
                    content[i] = new
       
        file.seek(index)
        for line in content:
            file.write(line)
            
    replace_capitalized_words("../CV-Builder-client/ihope.txt", data)
    compileText()
    # Compile LaTeX to PDF
    compile_latex_to_pdf(latex_file_path)
    return jsonify({"message": "success"})









    

if __name__ =="__main__":
    app.run(port=5000, debug=True)
