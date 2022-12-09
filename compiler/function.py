
from common.common import search_for
from compiler.attribution import Attribution


class Function():
    
    def __erro__(self):
        t = self.__token__
        print(f"Erro token {t} linha {t.row} coluna {t.col}")
    
    def __get_token__(self):
        self.__token__ = None if len(self.__tokens__) == 0 else self.__tokens__.pop(0)
    
    def __E__(self):
        self.__get_token__()
        if self.__token__.type == "TYPES":
            self.__get_token__()
            if self.__token__.type == "ID":
                found = search_for("(",")",self.__tokens__)
                Attribution()(found['exp'],parameter_declaration = True)
                self.__tokens__ = found['tokens']
                found = search_for("{","}",self.__tokens__)
                from compiler.block import Block
                Block()(found['exp'])
                self.__tokens__ = found['tokens']                
            else:
                self.__erro__()

        else:
            self.__erro__()
    def __call__(self,tokens):
        self.__tokens__ = tokens
        self.__E__()
        return self.__tokens__