class Transport:
    def travel(self):
        pass

class Train(Transport):
    def travel(self):
        print("Travelling by Train...")

class Plane(Transport):
    def travel(self):
        print("Travelling by Plane...")

t = Train()
p = Plane()

t.travel()
p.travel()
