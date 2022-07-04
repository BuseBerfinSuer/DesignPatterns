import random

class Shape():
    
    def factory(type):
        if type == "Circle": return Circle()
        if type == "Square": return Square()

class Circle(Shape):
    def draw(self):
        print("circle.draw" )
        
    
class Square(Shape):
    def draw(self):
        print("square.draw")
        
        
def shapeName(n):
    types = Shape.__subclasses__()
    for i in range(n):
        yield random.choice(types).__name__
shapes = [ Shape.factory(i) for i in shapeName(3)]


for shape in shapes:
    shape.draw()


class Shape2():
    
    def factory(type):
        if type == "Blue": return Blue()
        if type == "Red": return Red()

class Blue(Shape2):
    def color(self):
        print("Blue.color" )
       
class Red(Shape2):
    def color(self):
        print("Red.color")
        
def shapeColor(n):
     types = Shape2.__subclasses__()
     for i in range(n):
         yield random.choice(types).__name__        


shapes = [ Shape2.factory(i) for i in shapeColor(3)]   
  
for shape2 in shapes:
    shape2.color()