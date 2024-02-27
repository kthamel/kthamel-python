class DogClass:
    name = ""
    age = ""

    def set_name(self, name):
        self.name = name

    def bark(self, message): 
        msg = f"My name is {self.name}. {message}" # Self attribute is referencing to the class object and, can fetch the values from it.
        print(msg)

dog_1 = DogClass() 
dog_1.set_name("Cooby") 
dog_1.bark("mmmh")

dog_2 = DogClass() 
dog_2.set_name("Scooby") 
dog_2.bark("hih hih")
