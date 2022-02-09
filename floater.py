# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


#from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey): 
    radius = 5 
    def __init__(self,x,y):
        self.a = random.random()*360
        self.b = 5
        Prey.__init__(self, x, y, 10, 10, self.a, self.b)
    def update(self):
        if random.random() < 0.3:
            self.b = random.uniform(self.b-0.5,self.b+0.5)
            if self.b <3:
                self.b = 3
            if self.b >7:
                self.b = 7
            self.a = random.uniform(self.a-0.5,self.a+0.5)
            if self.a <3:
                self.a = 3
            if self.a >7:
                self.a = 7
            Prey.__init__(self, self._x, self._y, 10, 10, self.a, self.b)
        else:
            self.move()
    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius     , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill='red')
