import json
import re
from .log import *

with open("lexical/tokens/regex.json", 'r') as f:
    reg = json.load(f)
with open("lexical/tokens/separators.json", 'r') as f:
    sep = json.load(f)
    for i in sep:
        if i !="EVERY":
            sep[i] += sep["EVERY"]        
with open("lexical/tokens/types.json", 'r') as f:
    typ = json.load(f)
with open("lexical/tokens/reserved_words.json", 'r') as f:
    res = json.load(f)
spaces = [' ','\t','\n']
    
class Lexical(object):

    def __token_type__(t = None,err=True):
        if not t:
            t = Lexical.__word__
        if err and not Lexical.__valid__:
            return "ERROR"
        _type = []
        for i in reg:
            if re.search(reg[i],t):
                _type.append(i)
        _type = _type if not _type or len(_type)>1 else _type[0]
        return _type if len(_type) else None

    def __isseparator__(token_sep:str,c:str,token_analyze:str):
        return c in sep[token_sep] or token_analyze in sep[token_sep]

    # def __token__(char)-> dict:
    #     pass
    def __check_comment__(char):
        if Lexical.__comment__ and char == '\n':
            Lexical.__comment__ = False
        elif char == "#":
            Lexical.__comment__ = True
            Lexical.__word__ = ""
            Lexical.__token_types__ = None
        return Lexical.__comment__

    def __make_error__(char)-> bool:
        if Lexical.__isseparator__("ERROR",char,Lexical.__token_type__(char,False)):
            Lexical.__error__["token"] = Lexical.__word__
            Lexical.__log__.add_error(**Lexical.__error__)
            Lexical.__word__ = ""
            Lexical.__valid__ = True
            Lexical.__last_token__ = Lexical.__token_types__ = None
            return False
        else:
            Lexical.__word__+=char
            return True

    def __check_word__(char):
        w = Lexical.__word__
        possible_literal = not Lexical.__last_token__ and (w[0] == '"' or w[0]=="'")
        return (possible_literal or Lexical.__token__) and char != '\n'

    def __create_token__(col,row,char = None):
        Lexical.__token__ = Lexical.__token_type__()
        if char and not Lexical.__token__ and not (char== '"' or char=="'"):
            Lexical.__error__ = {"col":col,"row":row}
            return False
        separator = sep[Lexical.__token__]
        if char: 
            char_token_type = Lexical.__token_type__(char)
            if char not in separator and char_token_type not in separator:
                Lexical.__error__ = {"col":col,"row":row}
                return False
        if Lexical.__token__ == "ID":
            if Lexical.__word__ in res:
                Lexical.__token__ = "RESERVED"
            elif Lexical.__word__ in typ:
                Lexical.__token__ = "TYPES"
        Lexical.__log__.add_token(token=Lexical.__word__,type=Lexical.__token__)
        return True

    def __generate_token__()-> LexicalLog:
        col,row=-2,0
        for i in Lexical.__data__:

            col+=1
            if i == '\n':
                row+=1
                col=-2

            if not Lexical.__valid__:
                if Lexical.__make_error__(i):
                    continue
            if Lexical.__check_comment__(i):
                continue

            if Lexical.__word__ == "":
                    Lexical.__word__ = "" if i in spaces else i
            else:
                Lexical.__token__ = Lexical.__token_type__(Lexical.__word__+i)
                if Lexical.__check_word__(i):
                    Lexical.__word__+=i
                else:
                    if not Lexical.__last_token__:
                        Lexical.__word__+=i
                    
                    Lexical.__valid__ = Lexical.__create_token__(col,row,i)
                    if Lexical.__valid__:
                        Lexical.__word__ = "" if i in spaces else i
                    elif Lexical.__last_token__:
                        Lexical.__word__+=i
            Lexical.__last_token__ = Lexical.__token_type__()
            
    
    def analyze(path)->None:
        
        with open(path) as file:
            Lexical.__data__ = file.read()

        Lexical.__valid__ = True
        Lexical.__error__={}
        Lexical.__token__=[]
        Lexical.__last_token__ = None
        Lexical.__token_types__ = None
        Lexical.__word__ = ""
        Lexical.__log__ = LexicalLog()
        Lexical.__comment__ = False
        
        Lexical.__generate_token__()
        if not len(Lexical.__log__.errors):
            Lexical.__log__.errors = None
            
__all__ = [
    "Lexical"
]