class Token():
    token:str
    row:int
    col:int
    token_type:str

    def __init__(self,**kwargs)-> None:
        for i in kwargs:
            setattr(self,i,kwargs[i])

class LexicalLog():
    def __init__(self):
        self.errors = []
        self.tokens = []

    def add_token(self,**kwargs)->None:
        self.tokens.append(Token(**kwargs))
    
    def add_error(self,**kwargs)->None:
        self.errors.append(Token(**kwargs))

__all__ = [
    "LexicalLog",
    "Token"
]