class Lesson(object):
    
    def displayLesson(self, user, lesson_name):
        print("{}'s lesson: {}".format(user, lesson_name))
 
class User(object):
 
    def __init__(self, name):
        self.name = name
        self.lesson = Lesson()
 
    def sendLesson(self, lesson_name):
        self.lesson.displayLesson(self, lesson_name)
 
    def __str__(self):
        return self.name
 
Ali = User('Ali')   
Zeynep = User('Zeynep') 

 
Ali.sendLesson("Math")
Zeynep.sendLesson("Chemistry")
