class Animals():
    def __init__(self, breed):
        print("Greetings from Animal")
        self.breed = breed

    def talk(self):
        print("Animal is talking.")
    
    def move(self):
        print("Animal is moving.")

class Mamals():
    def __init__(self, feed):
        print("Mamal drinks milk.")
        self.breed = feed
    
    def mamalLself(self):
        print("I'm Mamal.")

class Dogs(Animals, Mamals):    # Inhert the all from Animal class and Mamals class
    def __init__(self, sound='woof'):
        super(Dogs, self).__init__("Dogs")
        self.name = sound
    
    def set_name(self, name):
        self.name = name

dog_02 = Dogs('Cooby')
dog_02.mamalLself()             # Here calling the non-existing function inside the Dogs class. But, It will print the relevant value
                                # because of multiple inheritance.