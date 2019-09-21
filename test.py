import os

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
try:
    raise NameError('HiThere')
except NameError:
    print('hi')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


raise B()

try:
    pi = 3.14/0
except(ZeroDivisionError):
    pass
