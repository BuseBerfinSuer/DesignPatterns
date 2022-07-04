class MakeMeal:

   def prepare(self): pass
   def cook(self): pass
   def eat(self): pass
   def drink(self): pass

   def go(self):
      self.prepare()
      self.cook()
      self.eat()
      self.drink()

class MakeCake(MakeMeal):
   def prepare(self):
      print ("Prepare Cake")
   
   def cook(self):
      print ("Cook Cake")
   
   def eat(self):
      print ("Eat Cake")

class MakeCoffee(MakeMeal):
   def prepare(self):
      print ("Prepare Coffee")
   
   def drink(self):
      print ("Drink Coffe")

makeCake = MakeCake()
makeCake.go()

print ("\n")

makeCoffee = MakeCoffee()
makeCoffee.go()