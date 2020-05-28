import time
import functools

def time_execution(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            return f(*args, **kwargs)
        finally:
            overall_time = (time.time() - start_time)
            print(f'{f.__name__} took {overall_time:.2f} seconds to execute')
    return wrapper
