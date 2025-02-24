# target https://www.hindawi.org/books/(\d+/)?
# target https://www.hindawi.org/books/categories/[a-zA-Z.-_]/(\d+/)?


from collections.abc   import Iterator
from selectolax.parser import Node
from hindawi_dl.utils  import Book
from hindawi_dl.const  import URL
from .utils            import Scraper
import re







class AllBooksPage(Scraper):
    __max_pages:int
    __books_num:int



    def _node2Book(node:Node) -> Book:
        href = node.css_first('a').attributes['href']
        img  = node.css_first('img').attributes
        return Book(
	        id         = int( re.findall(r"/books/(\d+)/?", href)[0]),
	        title      = img['alt'].replace("كتاب بعنوان", '').strip(),
	        url        = URL + href,
	        cover_url  = img['src'].strip()
        )
        


    def _load_attr(self) -> tuple[int]:
        india2arbic = {
            '٠':'0',
            '١':'1',
            '٢':'2',
            '٣':'3',
            '٤':'4',
            '٥':'5',
            '٦':'6',
            '٧':'7',
            '٨':'8',
            '٩':'9',
        }

        raw_txt = self.tree.css_first(".pagination .stats p").text(strip=True)
        raw_txt = raw_txt.translate(str.maketrans(india2arbic))
        self.__books_num = int(re.findall(r'(\d+)\s*كتاب', raw_txt)[0])
        self.__max_pages = self.__books_num//20 + (self.__books_num%20>0)
        return self.__max_pages, self.__books_num



    def books(self) -> Iterator[Book]:
        all_books = self.tree.css(".books_covers ul > li")
        return map(AllBooksPage._node2Book, all_books)



    @property
    def max_pages(self) -> int:
        try:
            return self.__max_pages
        except AttributeError:
            return self._load_attr()[0]



    @property
    def books_num(self) -> int:
        try:
            return self.__books_num
        except AttributeError:
            return self._load_attr()[1]
            



        
        
    
