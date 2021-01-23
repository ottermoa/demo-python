import LMT_lib
from LMT_lib import *

LMT_lib.globals = globals()
LMT_lib.locals = locals()

def hello (a):
    print(f'hello {a}')

def condition():
    '''for'''
    return 5

string = 'mac'
LMT_lib.loop ('hello', ['string'])
