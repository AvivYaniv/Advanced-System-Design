import functools

def validate_types(**types):    
    _RETURN_VALUE_NAME_ = 'return_value'
    
    def decorator(f):
        arg_names = f.__code__.co_varnames[:f.__code__.co_argcount]
        
        @functools.wraps(f)
        def wrapper(*args, **kw): 
            
            for argname, argtype in types.items():
                if _RETURN_VALUE_NAME_ != argname:
                    argval = args[arg_names.index(argname)]
                    if not isinstance(argval, argtype):
                        raise ValueError(f'argument {argname!r} must be {argtype}')
                 
            rv = f(*args, **kw)
            
            argname = _RETURN_VALUE_NAME_
            argtype = types[argname]
            if not isinstance(rv, argtype):                
                raise ValueError(f'argument {argname!r} must be {argtype}')            
            
            return rv
        return wrapper
    return decorator
