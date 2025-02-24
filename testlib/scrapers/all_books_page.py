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
        max_pages = AllBooksPage(html).max_pages

        self.assertEqual(type(max_pages), int)
        self.assertTrue(max_pages>0)



    def test_books_num(self):
        books_num = AllBooksPage(html).books_num

        self.assertEqual(type(books_num), int)
        self.assertTrue(books_num>0) 


