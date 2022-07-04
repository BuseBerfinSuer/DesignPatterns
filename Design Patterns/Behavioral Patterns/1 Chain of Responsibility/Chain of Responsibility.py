class AbstractHandler(object):
 
    def __init__(self, nxt):
 
        self._nxt = nxt
 
    def handle(self, request):
 
        handled = self.processRequest(request)
 
        if not handled:
            self._nxt.handle(request)
 
    def processRequest(self, request):
 
        raise NotImplementedError('First implement it !')
 
class FirstHandler(AbstractHandler):
 
    def processRequest(self, request):
 
        if 'a' < request <= 'e':
            print("This is {} handling request '{}'".format(self.__class__.__name__, request))
            return True
 
 
class SecondHandler(AbstractHandler):
 
    def processRequest(self, request):
 
        if 'e' < request <= 'o':
            print("This is {} handling request '{}'".format(self.__class__.__name__, request))
            return True
 
 
class DefaultHandler(AbstractHandler):
 
    def processRequest(self, request):
 
        print("This is {}  that request '{}' .".format(self.__class__.__name__,
                                                                                          request))
        return True
 
class User:
 
    def __init__(self):
 
        initial = None
 
        self.handler = FirstHandler(SecondHandler(DefaultHandler(initial)))
 
    def agent(self, user_request):
 
        for request in user_request:
            self.handler.handle(request)
 
user = User()
string = "Hello"
requests = list(string)
user.agent(requests)
