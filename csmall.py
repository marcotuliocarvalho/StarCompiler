import sys
from lexical.lexical import *

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print("Deve ser especificado o arquivo a ser compilado!")
        exit(1)
    
    Lexical.analyze(sys.argv[1])

    if Lexical.__log__.tokens:
        print("*******Lexical Tokens*******")
        for i in Lexical.__log__.tokens:
            print(f"{i.type}: {i.token}")
    if Lexical.__log__.errors:
        print("*******Lexical Errors*******")
        for i in Lexical.__log__.errors:
            print(f"Token: {i.token} ({i.row},{i.col})")
    
    