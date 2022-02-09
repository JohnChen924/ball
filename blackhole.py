# The Black_Hole class is derived from Simulton; for updating it finds+removes
#   objects (of any class derived from Prey) whose center is contained inside
#   its radius (returning a set of all eaten simultons), and displays as a
#   black circle with a radius of 10 (width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model as m

class Black_Hole(Simulton):  
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, 20, 20)
        self.radius = 10
    def update(self):
        b = set()
        a = set()
        for i in m.balls:
            if type(i) != self.__class__:
                if Simulton.distance(self,i.get_location()) > self.radius:
                    a.add(i)
                else:
                    b.add(i)
            else:
                a.add(i)       
        m.balls = a
        return b
                
    def display(self,canvas):
        canvas.create_oval(self._x-self.radius     , self._y-self.radius,
                                self._x+self.radius, self._y+self.radius,
                                fill='black')
