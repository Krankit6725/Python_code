'''
    RECURSION - CALLING FUNCTION INSIDE FUNCTION
'''


'''

def python():
    print("python")
    python()

python()

'''

import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

n = 0
def python():
    global n
    n = n +1
    print("python", n)
    python()

python()