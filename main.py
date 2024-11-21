from abc import ABC, abstractmethod
class Geomatrical_shapes(ABC):
    def flipcart(self):
        pass
class Rectangle(Geomatrical_shapes):
    def flipcart(self):
        print('I have 4 vertices and they are of 90 degrees')
class Circle(Geomatrical_shapes):
    def flipcart(self):
        print('I have no vertices, but I have infinite chords')
class Square(Geomatrical_shapes):
    def flipcart(self):
        print('I have also 4 vertices and they also are of 90 degrees')
class Triangle(Geomatrical_shapes):
    def flipcart(self):
        print('I have 3 vertices and the angles may vary')
P=Rectangle()
P.flipcart()
Q=Circle()
Q.flipcart()
R=Square()
R.flipcart()
S=Triangle()
S.flipcart()
