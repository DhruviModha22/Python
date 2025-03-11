class Animal:
    def speak(self):
        print("Animals can make sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.speak()
d.bark()

c.speak()
c.meow()
