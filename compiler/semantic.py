from common.common import *
from compiler.code_generator import Code
class Line:
    def __init__(self,token,token_type,initialized = False):
        self.token = token
        self.id_type = token_type
        self.initialized = initialized

    def initialize(self):
        self.initialized = True

class Semantic:
    __tokens = []
    
    def __exist__(token):
        return Semantic.__get__(token) >= 0

    def __get__(token):
        for i in range(len(Semantic.__tokens)):
            if Semantic.__tokens[i].token.token == token.token:
                return i
        return -1

    def declaration(token,t):
        if not Semantic.__exist__(token):
            Code.declaration(token.token,t)
            Semantic.__tokens.append(Line(token,t))
            return True
        error(token,"Token já declarado")
        return False

    def initialize(token):
        i = Semantic.__get__(token)
        if i>=0:
            Semantic.__tokens[i].initialize()
        else:
            error(token,"Token não declarado")

    def initialized(token):
        i = Semantic.__get__(token)
        if i >= 0:
            init = Semantic.__tokens[i].initialized
            if not init:
                warning(token,"Token não inicializado")
        else:
            error(token,"Token não declarado")

    def init_cast():
        Semantic.__cast = "bool"

    def cast(token):
        if token.type == "ID":
            token = Semantic.__token__(token)
            if token:
                value_type = token.id_type
            else:
                value_type = 'undefined'
        else:
            value_type = convert[token.type]
        order = cast["order"]
        i = order.index(Semantic.__cast)
        j = order.index(value_type)
        if i < j:
            Semantic.__cast = value_type
        
    def get_cast():
        return Semantic.__cast

    def __token__(token):
        i = Semantic.__get__(token)
        if i > -1:
            return Semantic.__tokens[i]
        else:
            error(token,"Token não declarado")

    def can_cast(token,exp_type):
        accept = cast["accept"]
        t = Semantic.__token__(token)
        if t:
            if not exp_type in accept[t.id_type]:
                error(token,f"Cast não suportado! {exp_type} -> {t.id_type}")
                return False
        else:
            error(token,"Token não declarado")
            return False
        return True
