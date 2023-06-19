# Animal Class

class Animal:

    def __init__(self): # when you make this class all the next things are true

        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath at a time, in and out")

    def eat(self):
        print("Nom nom nom")

    def procreate(self):
        print("Time to find a mate")

    def move(self):
        print("Onwards and upwards")

# breathe is abstracted
# cat = Animal()
# cat.breathe()


