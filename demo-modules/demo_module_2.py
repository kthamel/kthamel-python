## Importing the inbuilt module ##
from os import path             # os is parent module and path is child module.

if path.exists('demo_module_0.py'): # Using the path child module, checking the given file is existing or not.
    print("File is there.")

else:
    print("File not found.")

## Can do the same thing as below ##

import os.path      # That means, import the same "from os import path". But when calling the module, call it as below.

if os.path.exists('demo_module_1.py'):
    print("File is there.")

## When the module name is too lengthy, can follow the below method ##

import os.path as xx

if xx.exists('demo_module_2.py'):
    print("File is there.")