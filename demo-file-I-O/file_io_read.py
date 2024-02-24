file = open("test.txt") # Can use open function to open a file in Python.
cont = file.read()      # Read is a available feature with a file.
print(cont)             # Once, print the "cont" variable, can read the whole file.
file.close()            # Always, keep in mind to close the file after reading.

file = open("test.txt")            
                        # If didnt specify the count inside the brackets, will print whole file.
cont_1 = file.read(5)   # Otherwise it will print the required count.
                        # Once, print the "cont" variable, can read the whole file.
print(cont_1)

file = open("test.txt")
cont_2 = file.readline() # From this, it will print only one line
print(cont_2)
file.close()

file = open("test.txt")
while True:
    cont_3 = file.readline() # Using the while loop, can read the file. line by line.

    if not cont_3: 
        break
    print(cont_3)

file = open("test.txt")
for line in file: # Also, for loop having the same functionality.
    print(line)

file.close