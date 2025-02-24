# target https://www.hindawi.org/books/(\d+/)?
# target https://www.hindawi.org/books/categories/[a-zA-Z.-_]/(\d+/)?


from collections.abc   import Iterator
from selectolax.parser import Node, HTMLParser
from hindawi_dl.utils  import Book
from hindawi_dl.const  import URL, india2arbic
import re







class AllBooksPage:
    __total_pages :int|None
    __total_books :int|None
    books_iterator:Iterator[Book]



    def __init__(self, htmlcode:str|bytes) -> None:
        parser = HTMLParser(htmlcode)

        self.books_iterator = map(
            AllBooksPage._node2Book,
            parser.css(".books_covers ul > li")
        )

        self.__total_pages = None
        self.__total_books = None
        self._load_attr(parser)


        



    def _node2Book(node:Node) -> Book:
        href = node.css_first('a').attributes['href']
        img  = node.css_first('img').attributes
        return Book(
	        id         = int( re.findall(r"/books/(\d+)/?", href)[0]),
	        title      = img['alt'].replace("كتاب بعنوان", '').strip(),
	        url        = URL + href,
	        cover_url  = img['src'].strip()
        )
        


    def _load_attr(self, parser:HTMLParser) -> tuple[int]:
        
        raw_txt = parser.css_first(".list-nested.parent.selected > li > a span.count").text(strip=True)
        self.__total_books = int(raw_txt.translate(str.maketrans(india2arbic)))
        self.__total_pages = self.__total_books//20 + (self.__total_books%20>0)



    def books(self) -> list[Book]:
        return list(self.books_iterator)


    @property
    def total_pages(self) -> int:
        """total pages number of all pages in the website"""
        return self.__total_pages
    



    @property
    def total_books(self) -> int:
        """total books that exists in the website."""
        return self.__total_books

            



        
        
    
