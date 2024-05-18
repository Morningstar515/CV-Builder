import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd='qtip515', database='CVBuilder')
mycursor = mydb.cursor()
mycursor.execute("select Templates from TemplateTable where keyid='test'")

for i in mycursor:
    print(mycursor)