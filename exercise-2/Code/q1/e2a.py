def trace(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f'enter {f.__name__}')
        try:
            return f(*args, **kwargs)
        finally:
            print(f'leave {f.__name__}')
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
