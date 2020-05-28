def trace(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        call = f'{f.__name__}('
        if args:
            call += ', '.join(repr(arg) for arg in args)
        if kwargs:
            call += ', '.join(f'{key}={value!r}' for key, value in kwargs.items())
        call += ')'
        print(f'enter {call}')
        try:
            result = f(*args, **kwargs)
            print(f'leave {call}: {result!r}')
            return result
        except Exception as error:
            print(f'leave {call} on error: {error}')
            raise
    return wrapper


def wraps(original):
    def fix(wrapper):
        wrapper.__name__ = original.__name__
        wrapper.__doc__ = original.__doc__
        return wrapper
    return fix

@trace
def inc(x):
    return x + 1

if __name__ == '__main__':
    import sys
    print(inc(int(sys.argv[1])))
    sys.exit()
