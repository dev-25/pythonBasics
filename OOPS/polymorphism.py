# Polymorphism is the ability of an object to take on different forms.

# CODE 1
# Dynamic polymorphism / runtime polymorphism
# occurs when the method to be called is decided at runtime. 
# This is achieved through method overriding.
class Animal:
    def speak(self):
        print("I am an animal")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

def main():
    animal = Animal()
    dog = Dog()
    cat = Cat()

    animal.speak()
    dog.speak()
    cat.speak()

if __name__ == "__main__":
    main()

# CODE 2
# Static polymorphism / compile-time polymorphism
# occurs when the method to be called is decided at compile time. 
# This is achieved through function overloading.
def add(x, y):
    return x + y

def add(x, y, z):
    return x + y + z

print(add(1, 2))
print(add(1, 2, 3))


