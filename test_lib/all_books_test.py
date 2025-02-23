# test scrapers/all_books_page,py

from requests            import get as GET
from hindawi_dl.scrapers import AllBooksPage
from unittest            import TestCase
from hindawi_dl.utils    import Book



html = GET('https://www.hindawi.org/books/').content


class TestAllBookPage(TestCase):
    def test_books(self):
        books = list(AllBooksPage(html).books())
        if self.assertTrue(len(books) > 0, "0 book was loaded"):
        
            bk = books[0]
            self.assertEqual(type(bk), Book)



