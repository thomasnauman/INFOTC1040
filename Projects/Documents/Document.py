class Document:
    __title = None
    __body = None
    __author = None


    def __init__(self, t, b, a):
        if type(t) == str:
            self.__title = t
        else:
            raise Exception("Title must be string")
        if type(b) == str:
            self.__body = b
        else:
            raise Exception("Body must be string")
        if type(a) == str:
            self.__author = a
        else:
            raise Exception("Author must be string")


    def get_title(self):
        return self.__title
    def get_body(self):
        return self.__body
    def get_author(self):
        return self.__author

