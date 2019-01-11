employee_file = open("employees.txt", "r")      #read
#open("employees.txt", "w")      #write
#open("employees.txt", "a")      #a for append
#open("employees.txt", "r+")     #read and write

print(employee_file.readable())
#print(employee_file.read())
#print(employee_file.readline())
#print(employee_file.readlines()[3])

for employee in employee_file.readlines():
    print(employee)



employee_file.close()           #closes the file