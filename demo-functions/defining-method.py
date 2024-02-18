def grade_calc(): # Use def for define a function.
    print("Hello")

grade_calc() # use the function name for call the function. Have to care about the indentation, otherwise no output.

#######################
x = 80

def grade_calc(): # Use def for define a function.
    if x >= 0 and x < 35:
        print("Failed")
    elif x >= 35 and x <55:
        print(" S Pass")
    elif x >= 55 and x <65:
        print("C Pass")  
    elif x >= 65 and x <75:
        print("B Pass")
    elif x >= 75 and x <=100:
        print("A Pass")  
    else:
        print("Very bad")

grade_calc() # Can calculate the grade of another value, from calling the function like this. Not a good practice.
x = 60
grade_calc()

#######################
## Calling the function with single value ##
#######################
def grade_calc(x): 
    if x >= 0 and x < 35:
        print("Failed")
    elif x >= 35 and x <55:
        print(" S Pass")
    elif x >= 55 and x <65:
        print("C Pass")  
    elif x >= 65 and x <75:
        print("B Pass")
    elif x >= 75 and x <=100:
        print("A Pass")  
    else:
        print("Very bad")

grade_calc(60) # When calling the function like this, we have to mention what is passing to the function.
grade_calc(80) # In here passing the x value and, then we have to put x on calling function.

#######################
## Calling the function with multiple values ##
#######################
def grade_calc(subject, x): 
    print("Subject =", subject)
    if x >= 0 and x < 35:
        print("Failed")
    elif x >= 35 and x <55:
        print(" S Pass")
    elif x >= 55 and x <65:
        print("C Pass")  
    elif x >= 65 and x <75:
        print("B Pass")
    elif x >= 75 and x <=100:
        print("A Pass")  
    else:
        print("Very bad")

grade_calc("Maths",60) # When calling the function with multiple values, have to pass into the correct order.
grade_calc("Phycics",80) # These passing values, aka "positional parameters"