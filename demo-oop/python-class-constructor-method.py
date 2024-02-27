class DogClass:
    name = "None"
    
    def __init__(self): # This is known as Constructor method of a class. When calling the function, by default this function is running.
        print("Hello")

    def set_name(self, name):
        self.name = name

    def bark(self, message): 
        msg = f"My name is {self.name}. {message}" # Self attribute is referencing to the class object and, can fetch the values from it.
        print(msg)

dog_1 = DogClass() 
dog_1.set_name("Cooby") 
dog_1.bark("mmmh")
#######################
print("\n")
## In above example, def __init__(self) function was not called manually, but its printing the message. Because, by default Its running ##
## We can make changes to this, __init__(self) function, In programming its called overriding. ##

class CatClass:
    
    def __init__(self):
        self.name = "None"

    def set_name(self, name):
        self.name = name

    def nhewww(self, message): 
        msg = f"My name is {self.name}. {message}"
        print(msg)

cat_1 = CatClass() 
cat_1.set_name("Kity") 
cat_1.nhewww("nhew nhew")

cat_2 = CatClass()
cat_2.nhewww("nhew nhew") # Here, calling the function, without set_name. But, Its printing the name as None.

######################
print("\n")
######################

class CatClass:
    
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def nhewww(self, message): 
        msg = f"My name is {self.name}. {message}"
        print(msg)

cat_1 = CatClass('Kity') # After modifyint the __init__() function as we required, we can cann the CatClass as a usual function.
cat_1.nhewww("nhew nhew")# That means, passing the values inside the bracket. If call it without value, it will be crashed.
                         # To avoid it, have to set default value inside the __init__(self, name="None")
