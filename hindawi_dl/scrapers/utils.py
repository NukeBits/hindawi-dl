from selectolax.parser import HTMLParser






class Scraper:
    def __init__(self, html_code:str|bytes) -> None:
        self.tree = HTMLParser(html_code)
