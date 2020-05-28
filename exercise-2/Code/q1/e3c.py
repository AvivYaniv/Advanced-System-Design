import functools
import collections

def cache(max_size):    
    def decorator(f):
        class LRUCache(collections.OrderedDict):
            def __init__(self, capacity=None):
                self.capacity = capacity                
        
            def get(self, key):
                try:
                    value = self.pop(key)
                    self[key] = value
                    return value
                except KeyError:
                    return None
        
            def set(self, key, value):
                try:
                    self.pop(key)
                except KeyError:
                    if self.capacity:
                        if len(self) >= self.capacity:
                            self.popitem(last=False)
                self[key] = value  
        
        f.cache = LRUCache(max_size)
        
        @functools.wraps(f)        
        def wrapper(*args, **kwargs):                    
            token = args + tuple(kwargs.items())
            value = f.cache.get(token)
            if value is None:
                value = f(*args, **kwargs)
                f.cache.set(token, value)
            return value                                           
        return wrapper
    return decorator

@cache(max_size=5)
def fib(n):
    print(f'computing fib({n})...')
    return n if n < 2 else fib(n-1) + fib(n-2)

if __name__ == '__main__':
    import sys
    print(fib.__name__)
    print(fib(int(sys.argv[1])))
    sys.exit()
