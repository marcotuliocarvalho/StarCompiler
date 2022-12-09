import json
import re
from colorama import init
from termcolor import colored 
init()

with open("common/regex.json", 'r') as f:
    reg = json.load(f)
with open("common/separators.json", 'r') as f:
    sep = json.load(f)
    for i in sep:
        if i !="EVERY":
            sep[i] += sep["EVERY"]        
with open("common/types.json", 'r') as f:
    typ = json.load(f)
with open("common/reserved_words.json", 'r') as f:
    res = json.load(f)
with open("common/logical.json", 'r') as f:
    log = json.load(f)
with open("common/expression_cast.json", 'r') as f:
    cast = json.load(f)
# with open("common/sintatic.json", 'r') as f:
#     all_rules = json.load(f)
spaces = [' ','\t','\n']

convert = {
    "INTEGER":"int",
    "FLOAT":"float",
    "CHAR":"char",
    "LITERAL":"string"
}

class Token():
    def __init__(self,**kwargs)-> None:
        self.token = None
        self.type = None
        for i in kwargs:
            setattr(self,i,kwargs[i])
    
    def __str__(self):
        return self.token
    
    def __eq__(self,t):
        return self.token == t.token
    
def is_terminal(terminals,token):
    return token.token in terminals or token.type in terminals

def search_for(first,last,tokens):
    new_exp = []
    n = 0
    for i in range(len(tokens)):
        n = n-1 if tokens[i].token == last else n
        n = n+1 if tokens[i].token == first else n
        new_exp.append(tokens[i])
        if n == 0:
            tokens = tokens[i+1:]
            break
    return {"tokens":tokens,"exp":new_exp[1:-1]} if n==0 else None

def search_for_token(token,tokens,f = lambda x:x.token):
    new_exp = []
    found = False
    for i in range(len(tokens)):
        if f(tokens[i])== token:
            tokens = tokens[i+1:]
            found = True
            break
        new_exp.append(tokens[i])
    return {"tokens":tokens,"found":found,"exp":new_exp}

def message(t,m,type,c):
    text = "Compilation Failed"
    if t:
        text = f"{type}: {t.token}({t.row},{t.col})"
    if len(m):
        text += f" -: {m}"
    print(colored(text,c))

def error(token,error = ""):
    message(token,error,"Error","red")
    
def warning(token, error=""):
    message(token,error,"Warning","yellow")
