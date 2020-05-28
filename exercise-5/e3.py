import types

def load(path):
    # Loading code from path
    with open(path, 'r') as content_file:
        code = content_file.read()
    
    # Creating module
    m = types.ModuleType('m')
    
    # Adding module the code
    exec(code, m.__dict__)
    
    return m
        