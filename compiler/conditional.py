# from compiler.block import *
from tracemalloc import start
from common.common import *
from compiler.logical import Logical
from compiler.code_generator import Code

class Conditional:
    
    def __init__(self,loop_conditional):
        self.__loop_conditional__ = loop_conditional

    def __erro__(self):
        t = self.__token__
        print(f"Erro token {t} linha {t.row} coluna {t.col}")
    
    def __get_token__(self):
        self.__token__ = None if len(self.__tokens__) == 0 else self.__tokens__.pop(0)
    
    def __E__(self,conditional):
        self.__get_token__()
        if self.__token__:
            if self.__token__.token == conditional:
                if conditional != "else":
                    found = search_for("(",")",self.__tokens__)
                    # Code.generate_conditional(Logical.match(found['exp']))
                    
                    Code.add_label_Conditional("BEGIN")
                    Logical.match(found['exp'])
                    Code.add_label("END_COND")
                    self.__tokens__ = found['tokens']

                self.__get_token__()
                if self.__token__.token == "{":
                    self.__tokens__.insert(0,self.__token__)
                    found = search_for("{","}",self.__tokens__)
                else:
                    found = search_for_token(";",self.__tokens__)
                    # tokens = found['tokens']
                
                self.__tokens__ = found['tokens']
                
                from compiler.block import Block
                Block(self.__loop_conditional__)(found['exp'])
                if conditional != "else":
                    if len(self.__tokens__) > 1 and self.__tokens__[0].token in ["else","elif"]:
                        self.__E__(self.__tokens__[0].token)

    def __call__(self,tokens):
        self.__tokens__ = tokens
        Code.start_conditional()
        self.__E__("if")
        Code.finish_conditional()
        return self.__tokens__