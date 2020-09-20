class Pet:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def show_data(self):
        return "Hi, I am a " + self.breed + ", I am " + self.color + " in color"

class Dog(Pet):
    def __init__(self, breed, color, age):
        super().__init__(breed, color)
        self.age = age

    #method overriding
    def show_data(self):
        return "Hi, I am a " + self.breed + ", I am " + self.color + " in color and my age is " + str(self.age)


d1 = Dog("mutt", "brown", 10)
print(d1.show_data())
