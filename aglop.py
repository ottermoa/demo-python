import LMT_lib
from LMT_lib import *

LMT_lib.globals = globals()
LMT_lib.locals = locals()

i = 1

def count():
    global i
    print(i)
    i=i+i

def condition():
    '''while'''
    return i <= 7

LMT_lib.loop('count')