# Showcasing Inheritance

from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__() # initialises the parent class
        self.cold_blooded = True
        self.tetrapod = None # Not all reptiles have 4 legs
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None # Not true for all reptiles

    def seek_heat(self):
        print("its chilly outside, I need a sunbed")

    def hunt(self):
        print("Hunting prey")

    def use_venom(self):
        print("If I have it I might as well use it")

    def attract_mate_through_scent(self):
        print("Time to put on aftershave")

bulbasaur = Reptile()

bulbasaur.seek_heat()
