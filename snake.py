# Showcasing Encapsulation

from reptile import Reptile


class Snake(Reptile):

    def __init__(self):
        super().__init__() # Inherit everything from reptile
        self.forked_tongue = True
        self.cold_blooded = True
        self.venom = None # Not all snakes are venomous
        self.limbs = False
        self.tetrapod = False

    def use_tongue_to_smell(self):
        print("Do I say it smells nice or tastes nice...?")

sidney = Snake()
# sidney.breathe() # Animal
# sidney.seek_heat() # Reptile
# sidney.use_tongue_to_smell() # Snake

