
from distutils.log import ERROR
import re
import json

separators,regex = {},{}
reserved,types = [],[]
spaces = [' ','\t','\n']
tokens,errors = [],[]

valid_token_type = True

def create_token(word,col,row,char = None)->bool:
    token_type = get_type(word)
    if char: 
        char_token_type = get_type(char)
        if char not in separators[token_type] and char_token_type not in separators[token_type]:
            errors.append({"col":col,"row":row})
            return False
    if token_type == "ID":
        if word in reserved:
            token_type = "RESERVED"
        elif word in types:
            token_type = "TYPES"
    tokens.append({"token":word,"type":token_type})
    return True

def get_type(word, check_for_error = True):
    if not valid_token_type and check_for_error:
        return ERROR
    token_type = None
    if not word:
        return
    for i in regex:
        if re.search(regex[i],word):
            if not token_type:
                token_type = []
            token_type.append(i)

    if token_type and len(token_type)==1:
        token_type = token_type[0]
    return token_type

def load_jsons():
    global regex
    global separators
    global types
    global reserved
    with open("tokens/regex.json", 'r') as f:
        regex = json.load(f)
    with open("tokens/separators.json", 'r') as f:
        separators = json.load(f)
    with open("tokens/types.json", 'r') as f:
        types = json.load(f)
    with open("tokens/reserved_words.json", 'r') as f:
        reserved = json.load(f)

def lexical_analyzer(path:str)->dict:
    global valid_token_type

    with open(path) as file:
        data = file.read()

    load_jsons()

    word = ""
    col,row = 0,1
    comment = False
    token_types,last_token_types= None,None
    for i in data:
        if not valid_token_type:
            if i in separators["ERROR"] or get_type(i,False) in separators["ERROR"]:
                errors[-1]["token"] = word
                word = ""
                valid_token_type = True
                last_token_types = token_types = None
            else:
                word+=i
                continue
        
        if comment and i == '\n':
            comment = False
        elif not comment:
            if i == "#":
                comment = True
                word = ""
                token_types = None
            else:
                if word == "":
                    word = "" if i in spaces else i
                else:
                    token_types = get_type(word+i)
                    if (
                            (not last_token_types and 
                                (word[0] == '"' or word[0]=="'")
                            ) or 
                            token_types
                        ) and i != '\n':
                        word+=i
                    else:
                        if not last_token_types:
                            word+=i
                        
                        valid_token_type = create_token(word,col,row,i)
                        if valid_token_type:
                            word = "" if i in spaces else i
                        else:
                            word+=i
                last_token_types = get_type(word)
            col+=1
        if i == '\n':
            row+=1
            col=0
    
    if word:
        create_token(word,col,row)

    return dict({"tokens":tokens,"errors":errors if len(errors) else None})

__all__ = [
    "lexical_analyzer",
]