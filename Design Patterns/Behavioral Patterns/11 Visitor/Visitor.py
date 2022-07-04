class Courses_At_Clg:
 
    def accept(self, visitor):
        visitor.visit(self)
 
    def teaching(self, visitor):
        print(self, "Taught by ", visitor)
 
    def studying(self, visitor):
        print(self, "studied by ", visitor)
 
 
    def __str__(self):
        return self.__class__.__name__
 

class Math(Courses_At_Clg): pass

 
class Visitor:
 
    def __str__(self):
        return self.__class__.__name__

class Instructor(Visitor):
    def visit(self, crop):
        crop.teaching(self)
 
 
class Student(Visitor):
    def visit(self, crop):
        crop.studying(self)
 
Math = Math()
 
instructor =Instructor()
student =Student()
 
Math.accept(instructor)
Math.accept(student)

