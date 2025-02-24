from selectolax.parser import HTMLParser
from hindawi_dl.utils  import Book
from hindawi_dl.const  import india2arbic 
import re





class BookPage:
    def __init__(self, htmlcode:str|bytes, url:str) -> None:
        BookPage._verify_url(url)
        self.url = url


        self._title     = None
        self._id        = None
        self._authors   = None
        self._cover_url = None
        self._content   = None
        self._pdf       = None
        self._epub      = None
        self._kfx       = None
        self._words     = None
        self._tags      = None
        
        self.tree = HTMLParser(htmlcode)

        

    def _verify_url(url:str|None) -> None:
        if not type(url) == str:
            raise TypeError("`self.url` is not a str")
        if not bool(re.findall(r"https://(www.)?hindawi.org/books/\d{4,}/?", url)):
            raise ValueError(f"Pattern not found in text: {url}")
 


    def book(self) -> Book:
        return Book(
            id    = self.id,
            title = '',
            url   = self.url,
        )
    


    @property
    def id(self) -> int:
        if self._id == None:
            self._id = int(re.findall(r'/books/(\d+)/?', self.url)[0])
        return self._id


    
    @property
    def title(self) -> str:
        if self._title == None:
            self._title = self.tree.css_first(".details h2").text(strip=True)
        return self._title 



    @property
    def cover_url(self) -> str:
        if self._cover_url == None: 
            self._cover_url = self.tree.css_first(".cover img").attributes['src'].strip()
        return self._cover_url



    @property
    def authors(self) -> list[str]:
        if self._authors ==  None:
            self._authors = [a.text(strip=True) for a in self.tree.css(".author > a")]
        return self._authors
    
    


    @property
    def content(self) -> str:
        if self._content == None:
            self._content = '\n'.join(div.text(strip=True) for div in self.tree.css(".content > div"))
        return self._content



    def _find_if_exists(self, id:str):
        a_tag = self.tree.css_first(f"#{id}")
        return None if a_tag == None else a_tag.attributes['href'].strip()



    @property
    def pdf(self):
        if self._pdf == None:
            self._pdf = self._find_if_exists('pdf')
        return self._pdf



    @property
    def kfx(self):
        if self._kfx == None:
            self._kfx = self._find_if_exists('kfx')
        return self._kfx



    @property
    def epub(self):
        if self._epub == None:
            self._epub = self._find_if_exists('epub')
        return self._epub



    @property
    def word_count(self) -> int:
        if self._words == None:
            elmnt = self.tree.css_first(".tags > li > span")
            if elmnt == None:
                self._words = 0
            else:
                text = elmnt.text(strip=True).translate(str.maketrans(india2arbic))
                self._words = int(''.join(re.findall(r"\d", text)))
        return self._words


    
    @property
    def tags(self) -> list[str]:
        if self._tags == None:
            self._tags = [a.text(strip=True) for a in self.tree.css(".tags > li > a")]
        return self._tags
