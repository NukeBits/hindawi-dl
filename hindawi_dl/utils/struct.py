


class Book:
    def __init__(
        self,
        id   :int,
        title:str,
        url  :str, 

        cover_url:str|None = None,

    ) -> None:
        self.id        = id
        self.title     = title,
        self.url       = url,
        self.cover_url = cover_url

