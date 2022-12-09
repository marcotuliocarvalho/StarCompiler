# from common.common import *
# from compiler.expression import *
# from compiler.attribution import *
# from compiler.conditional import *
# from compiler.logical import *
# from compiler.loop import *
from compiler.block import *

class Sintatic():

    def analyze(all_tokens):
        
        Block(Semantic())(all_tokens)
        