class Subject:
 
    
 
    def __init__(self):
 
        
 
        self._observers = []
 
    def notify(self, modifier = None):
 
        
 
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)
 
    def attach(self, observer):
 
       
 
        if observer not in self._observers:
            self._observers.append(observer)
 
    def detach(self, observer):
 
        
 
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
 
 
 
class Data(Subject):
 
    
 
    def __init__(self, name =''):
        Subject.__init__(self)
        self.name = name
        self._data = 0
 
    @property
    def data(self):
        return self._data
 
    @data.setter
    def data(self, value):
        self._data = value
        self.notify()
 
 
class HexViewer:
 
    
 
    def update(self, subject):
        print('Hex:{} has 0x{:x}'.format(subject.name, subject.data))
 

 
 
class DecimalViewer:
 
    
 
    def update(self, subject):
        print('Decimal:% s has% d' % (subject.name, subject.data))
 

 
obj1 = Data('Data 1')
obj2 = Data('Data 2')
 
view1 = DecimalViewer()
view2 = HexViewer()
obj1.attach(view1)
obj1.attach(view2)
obj2.attach(view1)
obj2.attach(view2)

 
obj1.data = 11
obj2.data = 3