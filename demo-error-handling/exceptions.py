from os import path

file_name = 'test_file.txt'

if path.exists(file_name):              # In here checking the file is existing or non existing.                 
    with open(file_name) as file:       # If existing it will print the lines of file.
        print(file.readlines())

else:
    print("File - " + file_name + " Not found") # If file is non existing, it will print this message.

## Try Catch logic ##

x = 10 
y = 0 

# print(z) # If run this, will prompt this error -> "ZeroDivisionError: division by zero", Using try catch can avoid crasing the program.

try:
    z = x/y
    print(z)
except:
    print("Something went wrong!!")

## Capture the specific error from Try Catch ##
x = 10 
y = 0 
file_name = 'test_file.txt'      

try:
    with open(file_name) as file:
        print(file.readlines())

except ZeroDivisionError:               # As we know, when deviding the number using Python, getting the "ZeroDivisionError", here 
    print("Error with input values")    # Expecting that error and print the error message for specific error.

## Exception ##
file_name = 'test_file1.txt'            # test_file1.txt is non-existing file

try:
    with open(file_name) as file:
        print(file.readlines())

except Exception:                       # Here using Exception to capture, common errors, other than except each error.
    print("Common error was found!!")

## Print error message with Exception ##
file_name = 'test_file2.txt'      

try:
    with open(file_name) as file:
        print(file.readlines())

except Exception as xerror:                     # Here assigning the error message as xerror variable name.
    print("Something went wrong", xerror)    # And printing the exact error with exception error message. 

## Finally ##
a = 2
b = 5
file_name = 'test_file3.txt'      

try:
    c = b/a
    print(c)
    with open(file_name) as file:
        print(file.readlines())

except Exception as xerror:              
    print("Something went wrong", xerror) 

finally:                # This called cleanup task, whatever was happened in the program, execute the program under finally block.
    print("Job done")
