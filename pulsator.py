# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole
import model


class Pulsator(Black_Hole): 
    def __init__(self,x,y):
        self.radius = 10
        self.time = 0
        Black_Hole.__init__(self, x, y) 
    def update(self):
        self.time += 1
        if self.time == 30:
            self.radius -= 0.5
            self.time = 0
        a = len(Black_Hole.update(self))
        if a > 0:
            self.radius += a/2
            self.time = 0
        if self.radius == 0:
            model.remove(self)
        return Black_Hole.update(self)
    def display(self, canvas):
        Black_Hole.display(self, canvas)
    
