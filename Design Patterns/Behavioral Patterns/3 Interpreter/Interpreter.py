
class AbstractExpression():
   
    @staticmethod
    def interpret():  """ Called recursively for each Abstract Expression     """

class Number(AbstractExpression):
   
    def __init__(self, value):
        self.value = int(value)

    def interpret(self):
        return self.value

    def __repr__(self):
        return str(self.value)

class Add(AbstractExpression):
    

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()

    def __repr__(self):
        return f"({self.left} Add {self.right})"

class Subtract(AbstractExpression):
    "Non-Terminal Expression"

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()

    def __repr__(self):
        return f"({self.left} Subtract {self.right})"


SENTENCE = "5 + 4 - 3 "
print(SENTENCE)


TOKENS = SENTENCE.split(" ")
print(TOKENS)

AST = []  

AST.append(Add(Number(TOKENS[0]), Number(TOKENS[2])))  
AST.append(Subtract(AST[0], Number(TOKENS[4])))       


AST_ROOT = AST.pop()
print(AST_ROOT.interpret())
print(AST_ROOT)