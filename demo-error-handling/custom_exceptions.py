class Human():
    def __init__(self, name, age):
        super().__init__()

        self.name = name
        self.age = age

    @staticmethod
    def get_human(name,age):
        if not name:
            print("Invalid Name")
            return
        if age < 0 or age >= 120:
            print("Invalid Age")
            return
        
        return(name,age)
    
human_1 = Human.get_human("Adam", 10)
print(human_1)

human_2 = Human.get_human("", 10)
print(human_2)

human_3 = Human.get_human("Adam", 150)
print(human_3)

human_4 = Human.get_human("", -10)
print(human_4)

## From above it will print the error ##

class Human_1():
    def __init__(self, name, age):
        super().__init__()

        self.name = name
        self.age = age

    @staticmethod
    def get_human(name,age):
        if not name:
            raise Exception("Invalid Name") # In here trowing the error. 
        if age < 0 or age >= 120:
            raise Exception("Invalid Age")  # In here trowing the error..
        
        return Human_1(name,age)

# human_5 = Human_1.get_human("Eve", -10)
# print(human_5)
try:                                        
    human_5 = Human_1.get_human("Eve", -10)
    print(human_5)

except Exception as xerr:
    print("New Error:", xerr)

# Have to use try catch, Otherwise remaining part of the program will not executed

print("After try catch part was executed")

## Create custom Execption ##

class CustomNameException(Exception):
    def __init__(self, xerror):
        super(CustomNameException, self).__init__(xerror)

class CustomAgeException(Exception):
    def __init__(self, xerror):
        super(CustomAgeException, self).__init__(xerror)

class HumanX():
    def __init__(self, name, age):
        super().__init__()

        self.name = name
        self.age = age

    @staticmethod
    def get_human(name,age):
        if not name:
            raise CustomNameException("Invalid Name, CustomNameException")  # Here calling the custom exception. 
        if age < 0 or age >= 120:
            raise CustomAgeException("Invalid Age, CustomAgeException")     # Here calling the custom exception. 
        
        return HumanX(name,age)

# human_5 = Human_1.get_human("Eve", -10)
# print(human_5)
try:                                        
    human_6 = HumanX.get_human("Eve", -10)
    print(human_6)

except Exception as xerror:
    print("New Error:", xerror)