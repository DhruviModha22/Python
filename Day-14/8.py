class Vehicle:
    def start(self):
        print("Starting vehicle...")

class Bike(Vehicle):
    def start(self):
        print("Starting Bike... Kick start!")

class Car(Vehicle):
    def start(self):
        print("Starting Car... Push button start!")

b = Bike()
c = Car()

b.start()
c.start()
