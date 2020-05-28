import functools

def trace(f=None, *, log=print):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            call = f'{f.__name__}('
            
            # Setting args & kwargs in function representation, for better trace
            if args:
                call += ', '.join(repr(arg) for arg in args)
            if kwargs:
                call += ', '.join(f'{key}={value!r}' for key, value in kwargs.items())
            call += ')'
            
            # Setting call counter,initializing it if not defined yet
            if not 'call_counter' in dir(f):
                f.call_counter = 0
            identation = f.call_counter * ' '
            f.call_counter += 1
            
            log(f'{identation}enter {call}')
            try:
                result = f(*args, **kwargs)
                log(f'{identation}leave {call}: {result!r}')
                return result
            except Exception as error:
                log(f'{identation}leave {call} on error: {error}')
                raise
            finally:        
                f.call_counter -= 1     
        return wrapper
    if f:
        return decorator(f)
    return decorator

def wraps(original):
    def fix(wrapper):
        wrapper.__name__ = original.__name__
        wrapper.__doc__  = original.__doc__
        return wrapper
    return fix

def write(line):
    open('/tmp/log', 'a').write(line + '\n')

@trace
def fib(n):
    return n if n < 2 else fib(n-1) + fib(n-2)

if __name__ == '__main__':
    import sys
    print(fib.__name__)
    print(fib(int(sys.argv[1])))
    sys.exit()
