# Showcasing Polymorphism

from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        print("okay, hand me the stretchy pants")

    def constrict(self):
        print("and squeeeeeeze")

    def climb(self):
        print("up we go")

peter = Python()

peter.breathe()
peter.eat()
peter.hunt()
peter.use_tongue_to_smell()
