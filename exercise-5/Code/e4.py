import os
import sys
import contextlib

@contextlib.contextmanager
def in_directory(path):
    old_wd = sys.path[0]        
    sys.path[0] = path
        
    oldpwd=os.getcwd()
    os.chdir(path)
    
    try: 
        yield
    except Exception as e:
        raise e
    finally:
        sys.path[0] = oldpwd
        
        os.chdir(oldpwd)  
