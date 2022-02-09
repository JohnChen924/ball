from simulton import Simulton
from prey import Prey
import model as m
from blackhole import Black_Hole
import math
#causes ball and floaters to increase/decrease speed based on the distance from the special ball
class Special(Simulton):
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, 2, 2)
        self.radius = 3
    def update(self):
        for i in m.balls:
            if Prey in i.__class__.__bases__:
                i.set_speed(150*math.pow(0.99,self.distance(i.get_location())))
    def display(self, canvas):
        canvas.create_oval(self._x-self.radius     , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill='purple')
