from compiler.expression import Expression
from common.common import *
from compiler.semantic import *
from compiler.code_generator import Code

class Attribution:
    def __init__(self):
        self.__token__ = None

    def __erro__(self):
        error(self.__token__)
    
    def __get_token__(self):
        self.__token__ = None if len(self.__tokens__) == 0 else self.__tokens__.pop(0)
    
    def __end_error__(self):
        if self.__end_instruction__:
            error(self.__token__,f"Esperado \";\"")
            
    def __T__(self):
        if self.__token__:
            if self.__token__.type == "ID":
                if self.__declaration__:
                    Semantic.declaration(self.__token__,self.__type__)
                    
                self.__id__ = self.__token__
                self.__get_token__()
                if self.__token__:
                    if self.__token__.token == "=":
                        Semantic.initialize(self.__id__)
                        self.__tokens__ = Expression.match(self.__tokens__)
                        if Semantic.can_cast(self.__id__,Expression.__type__):
                            Code.attribution(self.__id__.token)
                        self.__get_token__()
                    if self.__token__:
                        if self.__token__.token == ",":
                            self.__get_token__()
                            self.__T__()
                        elif self.__token__.token != ";":
                            self.__end_error__()
                    else:
                        self.__end_error__()
            else:
                self.__erro__()
    
    def __E__(self):
        self.__get_token__()
        if self.__token__:
            if self.__token__.type == "TYPES":
                self.__type__ = self.__token__.token
                self.__declaration__ = True
                if not self.__initializing__:
                    self.__erro__()
                self.__get_token__()
            self.__T__()
        else:
            self.__erro__()

    def __K__(self):
        self.__get_token__()
        if self.__token__.type == "TYPES":
            self.__type__ = self.__token__.token
            self.__get_token__()
            if self.__token__.type == "ID":
                    # if self.__type__:
                Semantic.declaration(self.__token__,self.__type__)
                self.__id__ = self.__token__
                self.__get_token__()
                if self.__token__:
                    if self.__token__.token == "=":
                        Semantic.initialize(self.__id__)
                        self.__tokens__ = Expression.match(self.__tokens__)
                        Semantic.can_cast(self.__id__,Expression.__type__)
                    if self.__token__:
                        if self.__token__.token == ",":
                            self.__K__()
                    else:
                        self.__end_error__()
        else:
            self.__erro__()

    def __call__(self,tokens,initializing = True,end_instruction = True,parameter_declaration = False):
        if len(tokens)>0:
            self.__type__ = None
            self.__declaration__ = False
            self.__tokens__ = tokens
            if parameter_declaration:
                self.__end_instruction__ = False
                self.__K__()
            else:
                
                self.__initializing__ = initializing
                self.__end_instruction__ = end_instruction
                self.__E__()
                return self.__tokens__