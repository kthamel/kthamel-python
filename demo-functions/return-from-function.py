def grade_calc(x, subject="none"): 
    print("Subject =", subject)    
    if x >= 0 and x < 35:
        return "Failed" # Return will pass the value to the function caller, and not printing.
    elif x >= 35 and x <55:
        return "S"
    elif x >= 55 and x <65:
        return "C"  
    elif x >= 65 and x <75:
        return "B"
    elif x >= 75 and x <=100:
        return "A"  
    else:
        print("Very bad")

grade_calc(60, "Maths")

############### Print return value ###############
def grade_calc(x, subject="none"): 
    print("Subject =", subject)    
    if x >= 0 and x < 35:
        return "Failed" 
    elif x >= 35 and x <55:
        return "S"
    elif x >= 55 and x <65:
        return "C"  
    elif x >= 65 and x <75:
        return "B"
    elif x >= 75 and x <=100:
        return "A"  
    else:
        print("Very bad")

return_value = grade_calc(60, "Maths") # From assign the calling function it to another value and can print it.
print(return_value)