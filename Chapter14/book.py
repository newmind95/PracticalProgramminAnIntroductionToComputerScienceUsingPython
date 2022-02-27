class Book:
    """Information about a book, including title, list of authors,
    publisher, ISBN, and price.
    """
    
    def __init__(self, title, authors, publisher, ISBN, price):
        """ (Book, str, list of str, str, str, number) -> NoneType

        Create a new book entitled title, written by the people in authors,
        published by publisher, width ISBN isbn and costing price dollars.
        
        >>> python_book = Book( \
                'Practical Programming', \
                ['Campbell', 'Gries', 'Montojo'], \
                'Pragmatic Bookshelf', \
                '978-1-93778-545-1', \
                25.0)
        >>> python_book.title
        'Practical Programming'
        >>> python_book.authors
        ['Campbell', 'Gries', 'Montojo']
        >>> python_book.publisher
        'Pragmatic Bookshelf'
        >>> python_book.ISBN
        '978-1-93778-545-1'
        >>> python_book.price
        25.0
        """
        
        self.title = title
        # Copy the authors list in case the caller modifies that list later.
        self.authors = authors[:]
        self.publisher = publisher
        self.ISBN = ISBN
        self.price = price


    def __str__(self):
        """ (Book) -> str

        Return a human-readable string representation of this book.
        """
        return f'''Title: {self.title}
Authors: {', '.join(self.authors)}
Publisher: {self.publisher}
ISBN: {self.ISBN}
Price: {self.price}'''
    
    
    def __eq__(self, other):
        """(Book, Book) -> bool

        Return true iff this book and other book have same ISBN.
        """
        return self.ISBN == other.ISBN
        
    
    def num_authors(self):
        """(Book) -> int
        Returns the number of authors of this book.
        """
        
        return len(self.authors)
    
python_book1 = Book(
    'Practical Programming',
    ['Campbell', 'Gries', 'Montojo'],
    'Pragmatic Bookshelf',
    '978-1-93778-545-1',
    25.0)

python_book2 = Book(
    'Practical Programming',
    ['Campbell', 'Gries', 'Montojo'],
    'Pragmatic Bookshelf',
    '978-1-93778-545-1',
    25.0)
survival_book = Book(
    "New Programmer's Survival Manual",
    ['Carter'],
    'Pragmatic Bookshelf',
    '978-1-93435-681-4',
    19.0)

print('python_book1 instance')
print(python_book1)
print('python_book2 instance')
print(python_book2)
print(python_book1==python_book2)
print(python_book1==survival_book)
print(python_book2==survival_book)