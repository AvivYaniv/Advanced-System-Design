import functools

def cache(f):
    f.cache = {}
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        token = args + tuple(kwargs.items())
        if token not in f.cache:
            f.cache[token] = f(*args, **kwargs)
        return f.cache[token]
    return wrapper

@cache
def fib(n):
    print(f'computing fib({n})...')
    return n if n < 2 else fib(n-1) + fib(n-2)

if __name__ == '__main__':
    import sys
    print(fib.__name__)
    print(fib(int(sys.argv[1])))
    sys.exit()
