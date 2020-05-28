class Suppress:
    def __init__(self, *args):
        self.excpetions_types_to_supress = args
        
    def __enter__(self):
        return self
    
    def __exit__(self, exception, error, traceback):
        if not self.excpetions_types_to_supress:
            return True
        elif exception not in self.excpetions_types_to_supress:
                raise exception
        return True
    