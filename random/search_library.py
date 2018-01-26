"""
Given a corpus of book data in a specific format, write a Library class and a
search method to return a list of books given a specific word.

Note that the search should only work for whole words - searching for "tooth"
will only return books that contain "tooth" and not "toothbrush" or
"toothpaste".

eg:
>>> library = Library(LIBRARY_DATA)
>>> books = library.search("Arrakis")
>>> len(books)
1
>>> books[0].title
'Dune'

>>> books = library.search("the")
>>> len(books)
3
>>> [book.title for book in books]
['Dune', "The Hitchhiker's Guide to the Galaxy", 'The Amazing Adventures of Kavalier & Clay']
"""

LIBRARY_DATA = """
TITLE: Dune
AUTHOR: Frank Herbert
SUMMARY: Set in the distant future amidst a feudal interstellar society in
which noble houses, in control of individual planets, owe allegiance to the
Padishah Emperor, Dune tells the story of young Paul Atreides, whose noble
family accepts the stewardship of the desert planet Arrakis. As this planet is
the only source of the oracular spice melange, the most important and valuable
substance in the universe, control of Arrakis is a coveted - and dangerous -
undertaking.

TITLE: The Hitchhiker's Guide to the Galaxy
AUTHOR: Douglas Adams
SUMMARY: The series follows the adventures of Arthur Dent, a hapless
Englishman, following the destruction of the Earth by the Vogons, a race of
unpleasant and bureaucratic aliens, to make way for an intergalactic bypass.

TITLE: The Amazing Adventures of Kavalier & Clay
AUTHOR: Michael Chabon
SUMMARY: Joe Kavalier, a young Jewish artist who has also been trained in the
art of Houdini-esque escape, has just smuggled himself out of Nazi-invaded
Prague and landed in New York City. His Brooklyn cousin Sammy Clay is looking
for a partner to create heroes, stories, and art for the latest novelty to hit
America - the comic book. Drawing on their own fears and dreams, Kavalier and
Clay create the Escapist, the Monitor, and Luna Moth, inspired by the beautiful
 Rosa Saks, who will become linked by powerful ties to both men. With
exhilarating style and grace, Michael Chabon tells an unforgettable story about
 American romance and possibility.
"""


class Library:
    """Library class"""

    def __init__(self, data):
        """Instantiates book details in library."""

        data_by_books = data.splitlines()
        self.books = []

        for i, item in enumerate(data_by_books):
            if item == '':
                pass
            elif 'TITLE:' in item:
                try:
                    self.books.append(Book(title[1], author[1], summary))
                    title = item.split(': ')
                except:
                    title = item.split(': ')
            elif 'AUTHOR:' in item:
                author = item.split(': ')
            elif 'SUMMARY:' in item:
                summ = item.split(': ')
                summary = summ[1]
            elif i == (len(data_by_books) - 1):
                summary = summary + ' ' + item
                self.books.append(Book(title[1], author[1], summary))
            elif item != '':
                summary = summary + ' ' + item

    def __repr__(self):
        """Displays library details."""

        print('book1 = {}, book2 = {}'.format(self.books[0].title, self.books[1].title))

    def search(self, word):
        """Searches books for specific word."""

        books = []

        for item in self.books:

            if word in item.title:
                books.append(item)

            elif word in item.author:
                books.append(item)

            elif word in item.summary:
                books.append(item)

        return books


class Book:

    def __init__(self, title, author, summary):
        """Instantiates book detail."""
        self.title = title
        self.author = author
        self.summary = summary

    def __repr__(self):
        """Displays book details."""

        print 'title:{}, author:{}'.format(self.title, self.author)

    def title(self):
        """Returns book title."""

        return self.title

    def author(self):
        """Returns author of book."""

        return self.author

    def summary(self):
        """Returns summary of book."""

        return self.summary


################################################################################

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
