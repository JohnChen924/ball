# The Hunter class is derived (in order) from both Pulsator and Mobile_Simulton.
#   It updates/displays like its Pulsator base, but is also mobile (moving in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import random
import model as m
from simulton import Simulton
from blackhole import Black_Hole

class Hunter(Pulsator, Mobile_Simulton):  
    def __init__(self,x,y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, 10, 10, random.random()*360, 5)
    def update(self):
        a = set()
        for i in m.balls:
            if Prey in i.__class__.__bases__:
                if Simulton.distance(self,i.get_location()) < 200:
                    a.add((i,Simulton.distance(self,i.get_location())))
        if len(a) != 0:
            a = sorted(a,key = lambda x:x[1])
            a = a[0]
            angle = atan2(a[0]._y-self._y,a[0]._x-self._x)
            Mobile_Simulton.__init__(self, self._x, self._y, 10, 10,angle, 5)
            self.move()
        Pulsator.update(self)
        
    def display(self, canvas):
        Pulsator.display(self, canvas)
