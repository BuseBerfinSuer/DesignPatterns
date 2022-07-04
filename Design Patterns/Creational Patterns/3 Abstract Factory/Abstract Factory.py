import random
 
class book:
 
 
    def __init__(self, books_factory = None):
       
 
        self.book_factory = books_factory
 
    def show_book(self):
 
 
        book = self.book_factory()
 
        print(f'We have a book named {book}')
        print(f'its price is {book.price()}')

class Hamlet:
 
    def price(self):
        return 30
 
    def __str__(self):
        return "Hamlet"
 
class Ulysses:
 
    def price(self):
        return 80
 
    def __str__(self):
        return "Ulysses"
 
class MobyDick:
 
    def price(self):
        return 15
 
    def __str__(self):
        return 'MobyDick'
 
def random_book():
 
    
 
    return random.choice([MobyDick, Hamlet, Ulysses])()
 
 
if __name__ == "__main__":
 
    book = book(random_book)
 
    for i in range(1):
        book.show_book()