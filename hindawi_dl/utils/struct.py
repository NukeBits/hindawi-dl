


class Book:
    def __init__(
        self,
        id   :int,
        title:str,
        url  :str, 

        cover_url:str|None  = None,
        authors  :list[str] = [],
        content  :str       = '',
        pdf      :str|None  = None,
        kfx      :str|None  = None,
        epub     :str|None  = None,
        words    :int       = 0,
        tags     :list[str] = []


    ) -> None:
        self.id        = id
        self.title     = title
        self.url       = url
        self.cover_url = cover_url
        self.authors   = authors
        self.content   = content
        self.pdf       = pdf
        self.kfx       = kfx
        self.epub      = epub
        self.words     = words
        self.tags      = tags

