from compiler.attribution import Attribution
from common.common import *
from compiler.expression import Expression
from compiler.logical import Logical

class Loop:
        
    def __check__(self):
        self.__get_token__()
        found = search_for("(",")",self.__tokens__)
        self.__tokens__ = found['tokens']
        if self.__token__.token == "for":
            found = search_for_token(";",found['exp'])
            Attribution()(found['exp'],end_instruction=False)
            found = search_for_token(";",found['tokens'])
            Logical.match(found['exp'])
            Attribution()(found['tokens'],initializing=False,end_instruction=False)
        elif self.__token__.token == "while":
            Logical.match(found['exp'])
    
    def __erro__(self):
        t = self.__token__
        print(f"Erro token {t} linha {t.row} coluna {t.col}")
    
    def __get_token__(self):
        self.__token__ = None if len(self.__tokens__) == 0 else self.__tokens__.pop(0)
    

    def __E__(self):

        self.__check__()
        found = search_for("{","}",self.__tokens__)
        self.__tokens__ = found['tokens']
        from compiler.block import Block
        Block(True)(found['exp'])

    def __call__(self,tokens):
        self.__tokens__ = tokens
        self.__E__()
        return self.__tokens__