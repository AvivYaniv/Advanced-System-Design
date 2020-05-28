import functools

def exception_safe(*args):
    g, *other = args    
    exceptions_to_be_safe_for = Exception if not issubclass(type(g), type(Exception)) else args 
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*_args, **_kwargs):
            try:
                return f(*_args, **_kwargs)
            except exceptions_to_be_safe_for:
                return         
        return wrapper
    return decorator(g) if not issubclass(type(g), type(Exception)) else decorator

@exception_safe(NameError)
def sabich(error):
    raise error()

if __name__ == '__main__':
    import sys
    print(sabich.__name__)
    print(sabich(NameError))
    sys.exit()
