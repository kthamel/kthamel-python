# ## Access modifier type 01 - Public ##
class Human():
    def __init__(self, name):
        self.name = name
        self.age = 30

    def sleep(self):
        print("Zzzzz....", self.name)

man_1 = Human("man_1")
man_1.sleep()
print("Age of human is", man_1.age)
man_1.age = 50                      
print("Age of human is", man_1.age)

# ## Access modifier type 01 - Private ##
# class Human():
#     def __init__(self, name):
#         self.name = name
#         self.__age = 30 # Start the name of the variable name with two underscores 

#     def sleep(self):
#         print("Zzzzz....", self.name)

# man_1 = Human("man_1")
# man_1.sleep()
# print("Age of human is", man_1.__age) # Now, age is private and not accessible from out side.

## Fetch the value from the function ##
class Human():
    def __init__(self, name):
        self.name = name
        self.__age = 30
    
    def get__age(self):         # Using the get, can fetch the value of __age
        return self.__age

    def sleep(self):
        print("Zzzzz....", self.name)

man_1 = Human("man_1")
man_1.sleep()
print("Age of human is", man_1.get__age()) # Then call the get__age function to fetch age.

# ## Access modifier type 01 - Protected ##
class Human():
    def __init__(self, name):
        self.name = name
        self.__age = 30
        self._city = "Lisboa" # Here city was defined as Protected variable. begins with single underscore(_)
    
    def get__age(self):         
        return self.__age

class Man(Human):
    def my_city(self):
        print(self._city)

man_1 = Man("man_1")
man_1.my_city()                 # Here, calling the city
print("Age of human is", man_1.get__age())

