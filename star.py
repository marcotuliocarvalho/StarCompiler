import sys
from compiler.lexical import *
from compiler.sintatic import *
import json

if __name__ == "__main__":
    
    # if len(sys.argv) <= 1:
    #     print("Deve ser especificado o arquivo a ser compilado!")
    #     exit(1)
    
    Lexical.analyze("test.star")#sys.argv[1])
    Sintatic.analyze(Lexical.__log__.tokens)
    with open("intermediary.json","w") as file:
        file.write(json.dumps(Code.__code__))
    if Lexical.__log__.errors:
        print("*******Lexical Errors*******")
        for i in Lexical.__log__.errors:
            # pass
            print(f"Token: {i.token} ({i.row},{i.col})")
    
    