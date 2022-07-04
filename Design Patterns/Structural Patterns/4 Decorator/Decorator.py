class TextTag(object):
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text



class Italic(TextTag):
    

    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return "______ {} _______".format(self._wrapped.render())


simple_hello = TextTag("Design Patterns")
special_hello = Italic(simple_hello)
print("Before:", simple_hello.render())
print("After:", special_hello.render())

