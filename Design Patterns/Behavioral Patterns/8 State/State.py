class EmotionalState():
    
    def say_hello(self):
        pass

    
    def say_goodbye(self):
        pass
class HappyState(EmotionalState):
    def say_goodbye(self):
        return "Bye :)"

    def say_hello(self):
        return "Hello :)"
    
class SadState(EmotionalState):
    def say_goodbye(self):
        return "Bye :("

    def say_hello(self):
        return "Hello :("
    
class Person(EmotionalState):
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def say_goodbye(self):
        return self.state.say_goodbye()

    def say_hello(self):
        return self.state.say_hello()
    
    
person = Person(HappyState())
print("Hello in happy : " + person.say_hello())
print("Goodbye in happy : " + person.say_goodbye())

person.set_state(SadState())
print("Hello in sad : " + person.say_hello())
print("Goodbye in sad : " + person.say_goodbye())   
    
        