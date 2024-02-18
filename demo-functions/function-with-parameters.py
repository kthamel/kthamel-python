def grade_calc(x, subject="none"): # Here two input value is required, but calling the function with one value. 
    print("Subject =", subject)    # We must pass the values haven't the default parameter value.
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

grade_calc(60)
