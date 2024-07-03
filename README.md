
# Purpose:
  CV-Builder is a resume formatting tool used to easily integrate a users input on to popular resume templates.

# Requirements:
  **CV-Builder requires the user to initialize their own database**, but does provide a sql script (Data.sql) to set up and populate
  the database with the appropriate tables and values.

# How to run:
  Once the database is populated, user must then create a 'mysql.py' file with their database connection information listed respectively:
  
  *Replace values with valid information to access your database*
  
    def paswrd():
        return 'abc123'
    
    def host():
        return 'localhost'
    
    def user():
        return 'root'
    
    def databaseName():
        return 'nameOfYourDatabase'

**Place mysql.py file into root CV-Builder-server folder**

Once database setup is completed, start a separate terminal and navigate to /CV-Builder-server to run 'python server.py', starting the server
Then start a separate terminal and navigate to /CV-Builder-client to run 'npm run dev' to start client.
