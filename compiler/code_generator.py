
class Code:
    __code__ = []
    __label__ = {}
    __exp__ = 0
    __conditional__label__ = 0
    __conditional__label__control__ = 0

    def start_op():
        Code.__stack__ = []
        Code.__temp__ = 0
        Code.__exp__ = False

    def start_logical_op():
        Code.__stack_logical__ = []
        Code.__temp_logical__ = 0
        Code.__exp_logical__ = False

    def operator(op):
        assert(len(Code.__stack__)>=2)
        temp = f"t{Code.__temp__}"
        Code.__code__.append({
            "operation":op,
            "store":temp,
            "value 1":Code.__stack__.pop(),
            "value 2":Code.__stack__.pop(),
        })
        Code.__stack__.append(temp)
        Code.__temp__ += 1
        Code.__exp__ = True

    def operator_logical(op = None):
        assert(len(Code.__stack_logical__)>=1)
        temp = f"s{Code.__temp_logical__}"
        code = {
                "operation":"conditional",
                "logical":"!=",
                "value 1" : Code.__stack_logical__.pop(),
                "value 2":"0",
                "store":temp
            }
        if len(Code.__stack_logical__)>=1 and op:
            code["logical"] = op
            code["value 2"] = Code.__stack_logical__.pop()
            # code["logical"] = op[1]
        Code.__temp_logical__+=1
        Code.__code__.append(code)
        Code.__stack_logical__.append(temp)
    
    def set_value(op,k,v):
        for i in range(len(Code.__code__)-1,-1,-1):
            if Code.__code__[i]["operation"] == op:
                Code.__code__[i][k] = v
                break

    def operating_logical(op):
        Code.__stack_logical__.append(op)

    def finish_op_logical():
        if Code.__exp_logical__:
            last = Code.__code__.pop()
            last["store"] = f"exp"
            Code.__exp_logical__+=1
            Code.__code__.append(last)

    def operating(op):
        Code.__stack__.append(op)

    def finish_op():
        if Code.__exp__:
            last = Code.__code__.pop()
            last["store"] = f"exp"
            Code.__exp__+=1
            Code.__code__.append(last)

    def declaration(id,t):
        Code.__code__.append({
            "operation":"declaration",
            "var":id,
            "type":t
        })
    
    def attribution(id):
        Code.__code__.append({
            "operation":"attribution",
            "var":id,
            "local":f"exp{Code.__exp__}"
        })
    
    def function_return():
        Code.__code__.append({
            "operation":"return",
            "value":f"exp",
            "store":"func"
        })

    def start_conditional():
        Code.__conditional__ = []
        # Code.__is_conditional__ = True

    def finish_conditional():
        # Code.__is_conditional__ = False
        # Code.__code__ += Code.__conditional__
        Code.add_label_Conditional("END")

    def __get_label__(label,increment = True):
        if not label in Code.__label__:
            Code.__label__[label] = 0
        if increment:
            Code.__label__[label]+=1
        return f"{label}{Code.__label__[label]}"
    
    def add_label_Conditional(label):
        if label == "BEGIN":
            Code.__conditional__label__+=1
            count = Code.__conditional__label__
            Code.__conditional__label__control__=Code.__conditional__label__
        else:
            count = Code.__conditional__label__control__
            Code.__conditional__label__control__-=1
        Code.__code__.append({
            "operation":"label",
            "name":f"{label}{count}"
        })
    
    def add_label(label):

        Code.__code__.append({
            "operation":"label",
            "name":Code.__get_label__(label)
        })

    def generate_conditional(exp):
        temp = 0
        all_code = []
        if len(exp):
            cond = Code.__get_label__("COND")
        for i in exp:
            code = {
                "operation":"conditional",
                "logical":"!=",
                "jump":cond,
                "store":f"t{temp}"
            }
            temp+=1
            count = 0
            for j in i:
                if j.type == "LOGICAL_OPERATORS":
                    code["logical"] = j.token
                else:
                    code[f"value {count}"] = j.token
                    count+=1
            Code.__code__.append(code)
            all_code.append()
            # for j in i:
            #     if 
    # def start_logical():