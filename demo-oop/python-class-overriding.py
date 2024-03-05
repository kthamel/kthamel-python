class Animals():
    def __init__(self, breed):
        print("Greetings from Animal")
        self.breed = breed

    def talk(self):
        print("Animal is talking.")
    
    def move(self):
        print("Animal is moving")

class Dogs(Animals):
    def __init__(self, sound='woof'):
        super(Dogs, self).__init__("Dogs")
        self.name = sound
    
    def set_name(self, name):
        self.name = name
        print("I am a Dog")

    def set_name(self, move):
        super(Dogs, self).move() # Here overriding the Dogs class value from parent class value.
        print("I am running")

dog_02 = Dogs('Cooby')
dog_02.talk()
dog_02.move() # When calling the Dogs, will print "Animal is moving"