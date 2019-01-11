'''
if anything in the try block causes an error, the program
automatically returns the except blocks
'''

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
    value = number / 0
except ZeroDivisionError:
    print("Divided by zero")
except ZeroDivisionError as error:
    print(error)
except ValueError:
    print("Invalid Input")
