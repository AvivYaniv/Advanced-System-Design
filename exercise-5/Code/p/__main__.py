import sys

from .x.a import A
from .x.b import B
from .y.c import C
from .y.d import D

from .x.a import A
from .x.b import B
from .y.c import C
from .y.d import D
           
def _print_usage_and_exit():
    print('usage: <class_to_create>')
    sys.exit(0)
       
def main():
    if (2 != len(sys.argv)):
        _print_usage_and_exit()
        
    if (sys.argv[1] not in ['a', 'b', 'c', 'd']):
        _print_usage_and_exit()
        
    class_to_create = sys.argv[1]
    object_created  = None
    
    if 'a' == class_to_create:
        object_created = A()
    elif 'b' == class_to_create:
        object_created = B()
    elif 'c' == class_to_create:
        object_created = C()
    elif 'd' == class_to_create:
        object_created = D()
    
    print(f'created {object_created}')
            
if "__main__" == __name__:
    main()
    