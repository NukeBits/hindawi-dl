import re
from unittest                import TestCase
from hindawi_dl.scrapers     import BookPage
from requests                import get as GET
from hindawi_dl.utils.struct import Book


urls = [
    "https://www.hindawi.org/books/14842524/",
    "https://www.hindawi.org/books/26063085/",
]

html_files = [GET(url).content for url in urls]


class TestBookPage(TestCase):



    def test_url_assert(self):
        with self.assertRaises(TypeError):
            BookPage(html_files[0])
        with self.assertRaises(ValueError):
            BookPage(html_files[0], url="https://")
        with self.assertRaises(ValueError):
            BookPage(html_files[0], url="https://www.hindawi.org/book/123")
        BookPage(html_files[0], url=urls[1])
        BookPage(html_files[0], url="https://hindawi.org/books/3233424") # without www.


    
    def test_properties(self):
        for html in html_files:
	        bk = BookPage(html, urls[1])
	        self.assertTrue(bool(re.match(r'\d{3,}', str(bk.id))))
	        self.assertTrue(len(bk.title)>0)
	        self.assertTrue(bk.cover_url.startswith("https://downloads.hindawi.org/covers/"))
	        self.assertTrue(type(bk.authors)    == list)
	        self.assertTrue(bk.content          != ''  ) 
	        self.assertTrue(type(bk.content)    == str )
	        self.assertTrue(type(bk.word_count) == int )
	        self.assertTrue(type(bk.tags)       == list)
	        
	        
	
	
