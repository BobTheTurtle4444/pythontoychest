# 19.py - this program illustrates the use of function annotations in Python.
def parrot(voltage:str, state:str='a stiff', action:str='voom', type:str='Norwegian Blue') -> str:

    print("-- This parrot wouldn't", action, end=' ')

    print("if you put", voltage, "volts through it.")

    print("-- Lovely plumage, the", type)

    print("-- It's", state, "!")

    print(parrot.__annotations__)

parrot(1000)

parrot(voltage=1000)

parrot(voltage=1000000, action='VOOOOOM')

parrot(action='VOOOOOM', voltage=1000000)

parrot('a million', 'bereft of life', 'jump')

parrot('a thousand', state='pushing up the daisies')
