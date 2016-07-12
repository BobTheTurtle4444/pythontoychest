# 7.py - this program illustrates the use of default parameters in functions.
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
parrot(1000)                                         
parrot(voltage=1000)                               
parrot(voltage=1000000, action='VOOOOOM')             
parrot(action='VOOOOOM', voltage=1000000)            
parrot('a million', 'bereft of life', 'jump')        
parrot('a thousand', state='pushing up the daisies')
