from VECT_header import Vector

class point:
    def __init__(self,x1,y1):
        self.x1 = x1
        self.y1 = y1

    def distance(self,other):
        return ((self.x1 - other.x1)**2 + (self.y1 - self.y2))**(1/2)

    def p2v(self):    
        return Vector([self.x1, self.y1])
    