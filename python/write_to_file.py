#open("employees.txt", "r")      #read
#open("employees.txt", "w")      #write
#open("employees.txt", "a")      #a for append
#open("employees.txt", "r+")     #read and write

employee_file = open("employees1.txt", "w")     #write can be used to create a new file
employee_file.write("\nRonald - ICT")

employee_file.close()    

employee_file = open("index.html", "w")
employee_file.write("<p>This is html in python</p>")   #you can add html to python