import threading
import contextlib

class Extended(type):
    _THREAD_SAFE_FUNCTION_POSTFIX_      =   '_sync'
    _EXCEPTION_SAFE_FUNCTION_POSTFIX_   =   '_safe'
    
    @staticmethod
    def _toThreadSafeName(fname):
        return fname + Extended._THREAD_SAFE_FUNCTION_POSTFIX_

    @staticmethod
    def _toExceptionSafeName(fname):
        return fname + Extended._EXCEPTION_SAFE_FUNCTION_POSTFIX_
    
    def __init__(cls, name, bases, attrs):
        cls._lock = threading.Lock()
        for key, value in attrs.items():
            if not callable(value):
                continue
            thread_safe_value = synchronize(value, cls._lock)
            setattr(cls, Extended._toThreadSafeName(key), thread_safe_value)
            exception_safe_value = supress(value)
            setattr(cls, Extended._toExceptionSafeName(key), exception_safe_value)

def synchronize(function, lock):
    def wrapper(*args, **kwargs):
        with lock:
            return function(*args, **kwargs)
    return wrapper

def supress(function):
    def wrapper(*args, **kwargs):
        with contextlib.suppress(Exception):
            return function(*args, **kwargs)
    return wrapper
