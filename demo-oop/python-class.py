## This is a simple class, like a blue print. ##
class TestClass: # This is a class.
    pass

test1 = TestClass() # This called, create instance from class.
print(test1)

test1.name = "Tom" # Can assign any variable into the instance.
test1.age = 30
print(test1.name, test1.age)

##  Define a class with atributes. ##
class Dog:
    name = "" # These are called atributes of a class.
    age = ""
    breed = ""

dog1 = Dog()
dog1.name = "Cooby"
dog1.age = 4
dog1.breed = "cross"

print(dog1.name, dog1.age, dog1.breed)


## Create a class with actions ##
class Cat():
    name = ""

    def cat_function(self): # When defining the functions inside the classes, have to put "self as first parameter."
        print("nheww")

cat1 = Cat()
cat1.cat_function() # Here calling the cat_function, like this.

## Create a class with actions and calling with more attributes ##
class Cow():
    name = ""
    age = ""

    def cow_function(self, sound):
        print("Happy", sound)

cow1 = Cow()
cow1.cow_function("uumm") # Here, calling the cow_function with valus (uumm), inside the function it will indicate as sound.
