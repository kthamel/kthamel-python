print("Hello World") # This is single line commment.

"this is another single linecomment"

"""
This is
multi line 
comment
"""

def calculator(x,y):
    """
    Here we are going to devide x by y,
    x and y are integers.
    These is called as "doc string"
    """
    return x/y

def calculator(x: int, y: int):
    """
    Inside the function, defined the data type of x and y. 
    This called as type printhing of a function.
    """
    return x/y

def calculator(x: int=4, y: int=None):
    """
    If required to pass the default values with the the comment can pass it like above.
    """
    return x/y

z = calculator(10,2)
print(z)

