class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
 
    def get_rect_pr(self):
        # return 2*(self.w+self.h)
        print(2*(self.w+self.h))
  
class Square:
    def __init__(self, a):
        self.a = a
 
    def get_sq_pr(self):
        print (4*self.a)
    
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
 
    def get_tr_pr(self):
        print (self.a + self.b + self.c)
    
p = Rectangle(6,8)
p.get_rect_pr()

p = Square(8)
p.get_sq_pr()

p = Triangle(6,8,9)
p.get_tr_pr()

    