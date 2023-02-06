# Perimetra noteikšana
class Fig:
    def __init__(self, a=0, b=0, c=0, w=0, h=0):
        self.a = a
        self.b = b
        self.c = c
        self.w = w
        self.h = h

    def tr_pr(self):
        print (self.a + self.b + self.c)

    def sq_pr(self):
        print(4 * self.a)

    def rect_pr(self):
        p = self.w + self.h
        print(p)


Trijsturis = Fig(5,7,9)
Trijsturis.tr_pr()

Kvadrats = Fig(6)
Kvadrats.sq_pr()

Taisnsturis = Fig(10, 11, 3, 14, 12)
Taisnsturis.rect_pr()

