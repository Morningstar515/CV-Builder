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



## Dictionaries for appropriate Latex commands 
dicts = {

    "Jakes": {
        "end": r"\end{document}", 
        "education": "\\section{Education}  \n  \\resumeSubHeadingListStart  \n  \\resumeSubHeadingListEnd \n",

        "experience": "\\section{Experience} \n \\resumeSubHeadingListStart \n \\resumeSubHeadingListEnd \n",

        "projects": "\\section{Projects} \n \\resumeSubHeadingListStart \n \\resumeSubHeadingListEnd \n",
        "skills": "\\section{Technical Skills} \n \\resumeSubHeadingListStart \n \\resumeSubHeadingListEnd \n" 
    },
    "Stylish": {
        "end": r"\end{center}", 
        "education": r"""\section{Education}
            \begin{tabularx}{0.97\linewidth}{>{\raggedleft\scshape}p{2cm}X}

            \end{tabularx}
            """,
        "experience": r"""\section{Experience}
            \begin{tabularx}{0.97\linewidth}{>{\raggedleft\scshape}p{2cm}X}
        
            \end{tabularx}
            """,

        "projects": r"""\section{Projects}
            \begin{tabularx}{0.97\linewidth}{>{\raggedleft\scshape}p{2cm}X}

            \end{tabularx}
            """,
        "skills": r"""\section{Technical Skills}
            \begin{tabular}{ @{} >{\bfseries}l @{\hspace{6ex}} l }

            \end{tabular}
            """
    }
}


##Chosen Template
template = 'Jakes'

## Compile pdf
def compile_latex_to_pdf(latex_file_path):
    latex_dir = os.path.dirname(latex_file_path)
    os.chdir(latex_dir)
    subprocess.run(['pdflatex', '-interaction=nonstopmode', latex_file_path])
    latex_basename = os.path.splitext(os.path.basename(latex_file_path))[0]
    os.chdir("../CV-Builder-server/")

    # Return the path to the generated PDF file
    return os.path.join(latex_dir, f"{latex_basename}.pdf")

## Compile latex from txt
def compileText():
    with open('../CV-Builder-client/ihope.txt', 'r') as txt_file:
        content = txt_file.read()
    with open('../CV-Builder-client/ihope.tex', 'w') as tex_file:
            tex_file.write(content)

## Show Complete Page with selector values
def defaultPage(selectedTemplate):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute("select Templates from TemplateTable where keyid= %s ", (selectedTemplate,) )

    for i in mycursor:     
        with open("../CV-Builder-client/ihope.txt", "w") as file:

            # Write string to file
            file.write(i[0])

    compileText()
    compile_latex_to_pdf("../CV-Builder-client/ihope.tex")

## Get just the base tex from DB
def baseTex(template):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()

    mycursor.execute(f"select BaseTex from {template}Table")

    for i in mycursor:     
        with open("../CV-Builder-client/ihope.txt", "w") as file:

            # Write string to file
            file.write(i[0])
    compileText()
    compile_latex_to_pdf("../CV-Builder-client/ihope.tex")

## Helper function
def replace_capitalized_words(file_path, replacements):
    with open(file_path, 'r') as file:
        content = file.read()
    def replacer(match):
        word = match.group(0)
        return replacements.get(word, word)

    modified_content = re.sub(r'\b[A-Z][A-Z0-9]*\b', replacer, content)

    with open(file_path, 'w') as file:
        file.write(modified_content)



# Original Compile
latex_file_path = '../CV-Builder-client/ihope.tex'
defaultPage(template)


# Misc Routes
@app.route("/baseTex", methods=['GET', 'POST'])
def base():
    data = request.json
    baseTex(data["base"])
    return jsonify({"result": "success"})


@app.route("/default", methods=['GET', 'POST'])
def default():
    data = request.json
    defaultPage(data["template"])
    return jsonify({"result": "success"})


@app.route("/setTemplate", methods=['POST'])
def setTemplate():
    data = request.json
    global template 
    template = data["template"]
    return jsonify({"result": "success"})

## Banner Routes
@app.route("/addEducation", methods=['GET'])
def addEducationHeader():

    # Read file till insertion point found and end of document     
    with open("../CV-Builder-client/ihope.txt", "r") as file:
        content = file.readlines()
        index = 0
        for line in content:
            if dicts[template]["end"] in line:
                break;
            index += 1

        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            writeLine = 0
            for line in content:
                if writeLine == index:
                    file.write(dicts[template]["education"])
                
                # Write string to file
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
            if dicts[template]["end"] in line:
                break;
            index += 1

        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            writeLine = 0
            for line in content:
                if writeLine == index:
                    file.write(dicts[template]["experience"])

                # Write string to file
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
            if dicts[template]["end"] in line:
                break;
            index += 1

        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            writeLine = 0
            for line in content:
                if writeLine == index:
                    file.write(dicts[template]["projects"])

                # Write string to file
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
            if dicts[template]["end"] in line:
                break;
            index += 1

        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            writeLine = 0
            for line in content:
                if writeLine == index:
                    file.write(dicts[template]["skills"])

                # Write string to file
                file.write(line)
                writeLine += 1
    compileText()
    compile_latex_to_pdf(latex_file_path)
    return jsonify({"message":"success"})


##########################################################################################################

##########################    Parsing Data from each components input         ############################

##########################################################################################################


## Basics Section
@app.route("/parseBasics", methods=['POST'])
def parseBasics():
    data = request.data.decode("utf-8")
    data = json.loads(data)

    # Pull section from DB
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute(f"select Header from {template}Table")

    for i in mycursor:
        # Read file till insertion point found and end of document     
        with open("../CV-Builder-client/ihope.txt", "r") as file:
            content = file.readlines()
            index = 0

            for line in content:
                if dicts[template]["end"] in line:
                    break;
                index += 1
            content.insert(index ,i[0] + '\n')
            # Rewrite to file and insert new section at 'index' from previous loop
            with open("../CV-Builder-client/ihope.txt", "r+") as file:

                # Write string to file
                file.writelines(content)

    replace_capitalized_words("../CV-Builder-client/ihope.txt", data)
        
    compileText()

    # Compile LaTeX to PDF
    compile_latex_to_pdf(latex_file_path)

    return jsonify({"result": ""})

##############################################################################################################

## Education section
@app.route("/parseEducation", methods=['POST'])
def parseEducation():
    data = request.json

    # Pull section from DB
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute(f"select School from {template}Table")

    for i in mycursor:
        
        #Replacing ending number with correct entry number
        mod = i[0].replace('1',str(data["count"][0]))
        tup = (mod,)
        i = tup
   
        # Read file till insertion point found and end of document     
        with open("../CV-Builder-client/ihope.txt", "r") as file:
            content = file.readlines()

            #To account for latex headers with the same name, this prevents insertion unless we have passed the marker for a certain section
            pastLocationMarker = False
            index = 0
            for line in content:
                if "\\section{Education}" in line:
                    pastLocationMarker = True
                match = re.search(r'\\.*[E,e]nd.*$', dicts[template]["education"], re.MULTILINE)
                if match.group(0) in line and pastLocationMarker:
                    break;
                index += 1
            content.insert(index ,i[0] + '\n')

        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            file.writelines(content)

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
    mycursor.execute(f"select Experience from {template}Table")

    for i in mycursor:
    
        #Replacing ending number with correct entry number
        mod = i[0].replace('1',str(data["count"][0]))
        tup = (mod,)
        i = tup

        # Read file till insertion point found and end of document     
        with open("../CV-Builder-client/ihope.txt", "r") as file:
            content = file.readlines()
            file.seek(0)

            #To account for latex headers with the same name, this prevents insertion unless we have passed the marker for a certain section
            pastLocationMarker = False
            index = 0
            for line in content:
                if "\\section{Experience}" in line:
                    pastLocationMarker = True

                match = re.search(r'\\.*[E,e]nd.*$', dicts[template]["experience"], re.MULTILINE)
                if match.group(0) in line and pastLocationMarker:
                    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
                    break;
                index += 1
            content.insert(index ,i[0] + '\n')
            
        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            file.writelines(content)


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
        ## Remove unused bullets
        for line in content:
            if "EXPERIENCE" in line:
                continue

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
    mycursor.execute(f"select Projects from {template}Table")

    for i in mycursor:
        
        #Replacing ending number this correct entry number
        mod = i[0].replace('1',str(data["count"][0]))
        tup = (mod,)
        i = tup

        # Read file till insertion point found and end of document     
        with open("../CV-Builder-client/ihope.txt", "r") as file:
            content = file.readlines()

            #To account for latex headers with the same name, this prevents insertion unless we have passed the marker for a certain section        
            pastLocationMarker = False  
            index = 0
            for line in content:
                if "\\section{Projects}" in line:
                    pastLocationMarker = True

                match = re.search(r'\\.*[E,e]nd.*$', dicts[template]["projects"], re.MULTILINE)
                if match.group(0) in line and pastLocationMarker:
                    break;
                index += 1
            content.insert(index ,i[0] + '\n')

        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            file.writelines(content)


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

        ## Remove unused bullets
        for line in content:
            if "BULLET" in line:
                continue

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

    # Pull section from DB
    mydb = mysql.connector.connect(host="localhost", user="root", passwd=msql.user(), database='CVBuilder')
    mycursor = mydb.cursor()
    mycursor.execute(f"select Skills from {template}Table")

    for i in mycursor:
        
        #Replacing ending number with correct entry number
        mod = i[0].replace('1',str(data["count"][0]))
        tup = (mod,)
        i = tup

        # Read file till insertion point found and end of document     
        with open("../CV-Builder-client/ihope.txt", "r") as file:
            content = file.readlines()

            #To account for latex headers with the same name, this prevents insertion unless we have passed the marker for a certain section      
            pastLocationMarker = False  
            index = 0
            for line in content:
                if "\\section{Technical Skills}" in line:
                    pastLocationMarker = True

                if dicts[template]["end"] in line and pastLocationMarker:
                    break;
                index += 1
            content.insert(index ,i[0] + '\n')
        # Rewrite to file and insert new section at 'index' from previous loop
        with open("../CV-Builder-client/ihope.txt", "r+") as file:
            file.writelines(content)

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



############### Other helper functions #####################

def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str




    

if __name__ =="__main__":
    app.run(port=5000, debug=True)
