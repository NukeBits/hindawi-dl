# test scrapers/all_books_page.py

from requests            import get as GET
from hindawi_dl.scrapers import AllBooksPage
from unittest            import TestCase
from hindawi_dl.utils    import Book



html = GET('https://www.hindawi.org/books/categories/literary.criticism/').content


class TestAllBookPage(TestCase):
    def test_books(self):
        books = list(AllBooksPage(html).books())

        self.assertTrue(len(books) > 0, "0 book was loaded")
        self.assertEqual(type(books[0]), Book)



    def test_pages(self):
        total_pages = AllBooksPage(html).total_pages

        self.assertEqual(type(total_pages), int)
        self.assertTrue(total_pages>=175) # according to the last visit of website that should be correct 



    def test_total_books(self):
        total_books = AllBooksPage(html).total_books

        self.assertEqual(type(total_books), int)
        self.assertTrue(total_books>3000) 


