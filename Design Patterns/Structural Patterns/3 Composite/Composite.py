class Leaf:
  
    def __init__(self, *args):
  
        self.position = args[0]
  
    def show(self):
  
        
        print("\t", end ="")
        print(self.position)
  
  
class Composite:
  
    def __init__(self, *args):
  
        self.position = args[0]
        self.children = []
  
    def add(self, child):
  
        self.children.append(child)
  
    def remove(self, child):
  
        self.children.remove(child)
  
    def show(self):

        print(self.position)
        for child in self.children:
            print("\t", end ="")
            child.show()

  
top = Composite("School Principle")
sub1 = Composite("Teacher Mr. Black")
sub2 = Composite("Teacher Ms. Brown")
sub11 = Leaf("Class A1")
sub12 = Leaf("Class B1")
sub13 = Leaf("Class C1")
sub21 = Leaf("Class D1")
sub22 = Leaf("Class E1")
sub23 = Leaf("Class F1")
sub1.add(sub11)
sub1.add(sub12)
sub1.add(sub13)
sub2.add(sub21)
sub2.add(sub22)
sub2.add(sub23)
  
top.add(sub1)
top.add(sub2)
top.show()