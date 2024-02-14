# This step is initializing a dictionary. 
x = {
    '100': "Colombo",
    '101': "Negombo"
}

x['102'] = "Galle" # Add new element to a dictionary

print(x) # Print all the things inside the dictionary
print(x.keys()) # Print only keys of the dictionary
print(x.values()) # Print only values of the dictionary

y = x.get('110', 0) # From this, we can request the value of key='110' if it is non existing, will return 0
print(y)

del x['101'] # From this, we can delete a key from a dictionary
print(x)

x.clear() # From this. we can delete the dictionary.
print(x)