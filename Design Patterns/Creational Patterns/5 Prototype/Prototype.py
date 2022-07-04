import copy
 
class Courses_At_Clg():
     
    def __init__(self):
        self.id = None
        self.type = None

    def get_type(self):
        return self.type
 
    def get_id(self):
        return self.id
 
    def set_id(self, sid):
        self.id = sid
 
    def clone(self):
        return copy.copy(self)
 

class DSA(Courses_At_Clg):
    def __init__(self):
        super().__init__()
        self.type = "Data Structures and Algorithms"
 
    def course(self):
        print("Inside DSA::course() method")
        
    def clone(self):
        return copy.copy(self)
 

class SDE(Courses_At_Clg):
    def __init__(self):
        super().__init__()
        self.type = "Software Development Engineer"
 
    def course(self):
        print("Inside SDE::course() method.")
 
class STL(Courses_At_Clg):
    def __init__(self):
        super().__init__()
        self.type = "Standard Template Library"
 
    def course(self):
        print("Inside STL::course() method.")
 

class Courses_Cache:
     
    cache = {}
 
    
    def get_course(sid):
        COURSE = Courses_Cache.cache.get(sid, None)
        return COURSE.clone()
 
    
    def load():
        sde = SDE()
        sde.set_id("1")
        Courses_Cache.cache[sde.get_id()] = sde
 
        dsa = DSA()
        dsa.set_id("2")
        Courses_Cache.cache[dsa.get_id()] = dsa
 
        stl = STL()
        stl.set_id("3")
        Courses_Cache.cache[stl.get_id()] = stl
 

Courses_Cache.load()
 
sde = Courses_Cache.get_course("1")
print(sde.get_type())
 
dsa = Courses_Cache.get_course("2")
print(dsa.get_type())
 
stl = Courses_Cache.get_course("3")
print(stl.get_type())