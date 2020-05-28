import functools

def synchronize(lock):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            lock.acquire()
            try:
                return f(*args, **kw)
            finally:
                lock.release()
        return wrapper
    return decorator
