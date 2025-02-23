# target https://www.hindawi.org/books/


from collections.abc   import Iterator
from selectolax.parser import HTMLParser, Node
from hindawi_dl.utils  import Book
from hindawi_dl.const  import URL
import re


class Scraper:
    def __init__(self, html_code:str|bytes) -> None:
        self.tree = HTMLParser(html_code)






class AllBooksPage(Scraper):
    def _node2Book(node:Node) -> Book:
        href = node.css_first('a').attributes['href']
        img  = node.css_first('img').attributes
        return Book(
	        id         = int( re.findall(r"/books/(\d+)/?", href)[0]),
	        title      = img['alt'].replace("كتاب بعنوان", '').strip(),
	        url        = URL + href,
	        cover_url  = img['src'].strip()
        )
        
    
    def books(self) -> Iterator[Book]:
        all_books = self.tree.css(".books_covers ul > li")
        return map(AllBooksPage._node2Book, all_books)
    
