# It is the capability of one class to derive or inherit properties
# (methods & attribute) from parent class.

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("I am an animal!")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color
    def speak(self):
        print("Meow!")

def main():
    dog = Dog("Spot", "Golden Retriever")
    cat = Cat("Garfield", "Orange")
    dog.speak()
    cat.speak()

if __name__ == "__main__":
    main()