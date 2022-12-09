from numpy import isin
from compiler.expression import *
# from compiler.
# class Logical(object):
#     __logical__ = ["and","or","xor"]
#     __exp__ = []

#     def __valid__(exp):
#         count = 0
#         for i in exp:
#             if i.type == "LOGICAL_OPERATORS":
#                 count += 1
#                 if count > 1:
#                     error(i,"Expressão Lógica inválida!")
#         return len(exp) == 1 or count == 1

#     def __E__():
#         Logical.__expressions__ = []
#         for i in Logical.__exp__:
#             if not Logical.__valid__(i):
#                 continue
#             Logical.__expressions__.append(i)
#         # while len(Logical.__tokens__) > 0:
#         # f = search_for_token("LOGICAL_OPERATORS",Logical.__tokens__,lambda x:x.type)
#         # print(f)
#             # f1 = search_for_token("LOGICAL_OPERATORS",Logical.__tokens__,lambda x:x.type)
#             # f2 = search_for_token("LOGICAL",Logical.__tokens__,lambda x:x.type)
#             # if not f1['found'] or not f2['found']:
#             #     found = f1 if f1['found'] else f2    
#             # else:
#             #     found = f1 if len(f1['tokens']) > len(f2['tokens']) else f2
#             # tokens = found['tokens'] if not found["found"] else found["exp"]
#             # Expression.match(tokens)
#             # Logical.__tokens__ = found["tokens"]

#     def match(tokens):
#         exp = []
#         Logical.__exp__ = []
#         for i in tokens:
#             if i.type == "LOGICAL":
#                 Logical.__exp__.append(exp)
#                 exp = []
#             else:
#                 exp.append(i)
#         if len(exp):
#             Logical.__exp__.append(exp)
#         # Logical.__tokens__ = tokens
#         Logical.__E__()
#         return Logical.__expressions__
from compiler.expression import Expression

class Logical:
    __token__ = None
    def __get_token__():
        # if not Logical.__init__:
        Logical.__token__ = None if len(Logical.__exp__) == 0 else Logical.__exp__.pop(0)
        if Logical.__token__:
            if isinstance(Logical.__token__,list):
                exp = []
                separated = []
                for i in Logical.__token__:
                    if i.type == "LOGICAL_OPERATORS":
                        separated.append(exp)
                        separated.append(i)
                        exp = []
                    else:
                        exp.append(i)
                if len(exp):
                    separated.append(exp)
                if len(separated):
                    Expression.match(separated[0])
                    # Code.set_value("conditional","store","exp1")
                    Code.operating_logical("exp1")
                    if len(separated)>1:
                        Expression.match(separated[2])
                        # Code.set_value("conditional","store","exp2")
                        Code.operating_logical("exp2")
                        Code.operator_logical(separated[1].token)
                    else:
                        Code.operator_logical()
    
    def __valid__():
        if not isinstance(Logical.__token__,list):
            return False
        count = 0
        for i in Logical.__token__:
            if i.type == "LOGICAL_OPERATORS":
                count += 1
                if count > 1:
                    error(i,"Expressão Lógica inválida!")
        return len(Logical.__token__) == 1 or count == 1
    
    def __T__():
        if Logical.__token__:
            t = Logical.__token__
            if isinstance(t,list) or t.token == "(":
                Logical.__F__()
                Logical.__T2__()
            # elif not isinstance(t,list):
            #     error(t)
    
    def __F__():
        if Expression.__token__:
            t = Logical.__token__
            if not isinstance(t,list):
                if t.token == "(":
                    Logical.__E__()
                    # Logical.__get_token__()
                    if Logical.__token__:
                        t = Logical.__token__
                        if not isinstance(t,list):
                            if t.token != ")":
                                error(t,"Esperado \")\"!")
                        elif Logical.__valid__():
                            pass
            elif Logical.__valid__():
                pass

    def __T2__():
        Logical.__get_token__()
        if Logical.__token__:
            if Logical.__token__.token == "and":
                t = Logical.__token__
                Logical.__get_token__()
                Logical.__F__()
                Logical.__T2__()
                Code.operator_logical(t.token)
            else:
                Logical.__tokens__.insert(0,Logical.__token__)

    def __E2__():
        if Logical.__token__:
            Logical.__get_token__()
            if Logical.__token__.token == "or":
                Logical.__get_token__()
                Logical.__T__()
                Logical.__E2__()
                Code.operator_logical(Logical.__token__.token)
            elif Logical.__token__.token !=")":
                error(Logical.__token__,"Esperado \")\"!")


    def __E__():
        Logical.__get_token__()
        if Logical.__token__:
            if Logical.__valid__() or Logical.__token__.token == "(":
                Logical.__T__()
                Logical.__E2__()
            else:
                Logical.__get_token__()
                Logical.__E__()
            
        
    def match(tokens):
        Code.start_logical_op()
        exp = []
        Logical.__exp__ = []
        Logical.__token__ = None
        for i in tokens:
            if i.type == "LOGICAL" or i.token in ["(",")"]:
                if len(exp):
                    Logical.__exp__.append(exp)
                Logical.__exp__.append(i)
                exp = []
            else:
                exp.append(i)
        if len(exp):
            Logical.__exp__.append(exp)
        Logical.__E__()

        Code.finish_op_logical()
