import random

class Shape():
    
    def factory(type):
        if type == "Circle": return Circle()
        if type == "Square": return Square()

class Circle(Shape):
    def draw(self):
        print("circle.draw" )
        print("CIRCLE.draw" )
    
    
class Square(Shape):
    def draw(self):
        print("square.draw")
        print("SQUARE.draw")
    
    
def shapeName(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__

shapes = [ Shape.factory(i) for i in shapeName(5)]

for shape in shapes:
    shape.draw()
 