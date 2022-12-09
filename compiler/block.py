from asyncore import loop
from common.common import *
from compiler.expression import *
from compiler.attribution import *
from compiler.conditional import *
from compiler.logical import *
from compiler.loop import *
from compiler.function import *

class Block(object):
    def __init__(self,loop = False):
        self.__loop__ = loop

    def __erro__(self):
        error(self.__token__)
    
    def __get_token__(self):
        self.__token__ = None if len(self.__tokens__) == 0 else self.__tokens__.pop(0)
    
    def __E__(self = Semantic()):
        self.__warning_return__ = True
        while len(self.__tokens__) > 0:
            t = None if len(self.__tokens__) == 0 else self.__tokens__[0]
            if t:
                if t.token == "if":
                    self.__tokens__ = Conditional(self.__loop__)(self.__tokens__)
                elif t.type in ["ID","TYPES"]:
                    if t.type == "TYPES" and self.__tokens__[1].type == "ID" and self.__tokens__[2].token == "(" :
                        self.__tokens__ = Function()(self.__tokens__)
                    else:
                        self.__tokens__ = Attribution()(self.__tokens__)
                elif t.token in ["while","for"]:
                    self.__tokens__ = Loop()(self.__tokens__)
                elif t.token in ['break','continue']:
                    self.__tokens__.pop(0)
                    if not self.__loop__ :
                        self.__erro__()
                    if len(self.__tokens__) >=1:
                        if self.__tokens__[0].token == ";":
                            self.__tokens__.pop(0)
                        else:
                            error(self.__token__,f"Esperado ;")
                elif t.token == "return":
                    self.__get_token__()
                    
                    aux = Expression.match(self.__tokens__,True)
                    if len(self.__tokens__) != aux:
                        Code.function_return()
                    self.__tokens__ = aux
                    self.__get_token__()
                    if self.__token__.token != ";":
                        error(self.__token__,f"Esperado \";\"")
                    else:
                        if self.__warning_return__ and len(self.__tokens__):
                            warning(self.__tokens__[0],"Código Inalcançado")
                            self.__warning_return__ = False
                            
            
    def __call__(self,tokens):
        self.__tokens__ = tokens
        self.__E__()
