from common.common import *
from compiler.semantic import Semantic
from compiler.code_generator import Code


class Expression:
    
    # __errors__=[]
    __tokens__ = []
    __terminals__ = ["ID","FLOAT","INTEGER","LITERAL"]
    __token__ = None
    __init__ = False
    __errors__ = []
    __type__ = None
    
    def __erro__():
        if not Expression.__init__:
            t = Expression.__token__
            Expression.__init__ = True
            if not t in Expression.__errors__:
                Expression.__tokens__.insert(0,t)
                error(t)

    def __get_token__():
        if not Expression.__init__:
            Expression.__token__ = None if len(Expression.__tokens__) == 0 else Expression.__tokens__.pop(0)
            if Expression.__token__:
                if Expression.__token__.type in Expression.__terminals__:
                    Code.operating(Expression.__token__.token)
                
    def __T__():
        if Expression.__init__:
            return
        if Expression.__token__:
            t = Expression.__token__
            if t.token == "(" or t.type in Expression.__terminals__:
                if t.type == "ID":
                    Semantic.initialized(Expression.__token__)
                if t.token != "(":
                    Semantic.cast(t)
                Expression.__F__()
                Expression.__T2__()
            else:
                Expression.__erro__()

    def __E2__():
        if Expression.__init__:
            return
        Expression.__get_token__()
        if Expression.__token__:
            t = Expression.__token__

            if t.token == "+" or t.token == "-":
                Expression.__get_token__()
                Expression.__T__()
                Expression.__E2__()
                Code.operator(t.token)

            elif t.token != ")":
                Expression.__erro__()

    def __T2__():
        if Expression.__init__:
            return
        Expression.__get_token__()
        if Expression.__token__:
            t = Expression.__token__

            if t.token == "*" or t.token == "/":
                Expression.__get_token__()
                Expression.__F__()
                Expression.__T2__()
                Code.operator(t.token)
            else:
                Expression.__tokens__.insert(0,t)
    
    def __F__():
        if Expression.__init__:
            return
        if Expression.__token__:
            t = Expression.__token__
            if t.token == "(":
                Expression.__E__()
                # Expression.__get_token__()
                if Expression.__token__:
                    t = Expression.__token__
                    if t.token != ")":
                        Expression.__erro__()

    def __E__():
        if Expression.__init__:
            return
        Expression.__get_token__()
        if Expression.__token__:
            t = Expression.__token__
            if t.token == "(" or t.type in Expression.__terminals__:
                Expression.__T__()
                Expression.__E2__()
            else:
                Expression.__erro__()
                
    def match(tokens,is_return = False):
        Expression.__tokens__ = []
        Semantic.init_cast()
        Code.start_op()
        if not isinstance(tokens,list):
            tokens = list([tokens])
        while len(tokens):
            token = tokens[0]
            if not token or token.token in [",",";"]:
                break
            tokens.pop(0)
            if token:
                Expression.__tokens__.append(token)

        if not len(Expression.__tokens__):
            if not is_return:
                error(f"Esperado expressao")
        else:
            while True:
                Expression.__init__ = False
                Expression.__E__()
                if not Expression.__init__:
                    break
        
        Expression.__type__ = Semantic.get_cast()
        Code.finish_op()
            
        return tokens
