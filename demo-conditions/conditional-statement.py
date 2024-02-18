x = 100

if x > 150: # This is the condition. from the colan [:] we are starting the block.
    print("pass")
else:       # If the condition is not full-filling, return the else condition.
    print("fail")

###########
x = 75

if x > 75:
    result = "Pass"
else:
    result = "Fail"

print(result)

############
x = -10

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

#############
x = 100

if x < 0 or x > 100:
    print("Very Bad")
    exit() # Not recommended at all.

elif x < 35:
    print("Failed")
elif x <55:
    print(" S Pass")
elif x <65:
    print("C Pass")  
elif x <75:
    print("B Pass")
elif x <=100:
    print("A Pass")  

############## This called Ternary, Because this condition has 3 parts ############## 
height = 150

message = ("Your job is: ") + "Security" if height > 150 else "Labour"

print(message)