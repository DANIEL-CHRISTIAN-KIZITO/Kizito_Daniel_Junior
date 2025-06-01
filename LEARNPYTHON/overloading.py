#
from multipledispatch import dispatch

@dispatch(int, int)
def sum(r, w):
    s = r + w
    print(s)
@dispatch(int, int, int)
def sum(r, w, x):
    s = r + w + x
    print(s)
    
sum(2,3)
sum(2,3)
