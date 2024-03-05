class Animals():
    def __init__(self, breed):
        print("Greetings from Animal")
        self.breed = breed

    def talk(self):
        print("Animal is talking.")
    
    def move(self):
        print("Animal is moving")

class Dogs(Animals):    # Inhert the all from Animal class
    def __init__(self, sound='woof'):
        self.name = sound
    
    def set_name(self, name):
        self.name = name

dog_01 = Dogs('Cooby')  # Here calling the Dog function. 
dog_01.talk()           # Can see, no attribute under Dog class. When run this Python code, can see the "Animal is talking" as output.

print("\n")
## If, want to call the Parent  first and then the clid. Have to use the function called "super"
class Animals():
    def __init__(self, breed):
        print("Greetings from Animal")
        self.breed = breed

    def talk(self):
        print("Animal is talking.")
    
    def move(self):
        print("Animal is moving")

class Dogs(Animals):    # Inhert the all from Animal class
    def __init__(self, sound='woof'):
        super(Dogs, self).__init__("Dogs")
        self.name = sound
    
    def set_name(self, name):
        self.name = name

dog_02 = Dogs('Cooby')  # Here calling the Dog function. 
dog_02.talk()           # When executing this , can see the output "Greetings from Animal"