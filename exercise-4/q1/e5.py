import io
import os
import sys
import time
import shutil
import tempfile
import contextlib

class CReturnValue:
    pass
        
@contextlib.contextmanager
def timer():
    t = CReturnValue()
    t.started = time.time()       
    try: 
        yield t
    except Exception as e:
        raise e
    finally:    
        t.elapsed = time.time() - t.started    
        t.stopped = t.elapsed + t.started    

@contextlib.contextmanager
def suppress(*exceptions):
    try:
        yield
    except Exception if not exceptions else exceptions:
        pass
        
@contextlib.contextmanager
def standard_output():
    _original_stdout = sys.stdout 
    sys.stdout = io.StringIO()
    v = CReturnValue()
    try:        
        yield v
    finally:
        v.value = sys.stdout.getvalue()
        sys.stdout = _original_stdout
        
@contextlib.contextmanager
def temporary_file():
    f, _ = tempfile.mkstemp()    
    try:        
        yield f
    finally:
        os.close(f)

@contextlib.contextmanager
def temporary_directory():
    d = tempfile.mkdtemp()    
    try:        
        yield d
    finally:
        shutil.rmtree(d) 
