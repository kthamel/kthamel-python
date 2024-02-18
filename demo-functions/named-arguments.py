def grade_calc(x=0, subject="none"): # We can set default parameters for both input values. 
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

grade_calc(subject="Maths", x=60) # But, when calling the function have to define which value is passing. Order doesn't matter.

