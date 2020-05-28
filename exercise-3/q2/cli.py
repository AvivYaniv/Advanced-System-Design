import functools

class CommandLineInterface:
    
    def command(self, f):
        setattr(self, f.__name__, f)        
    
    @staticmethod
    def info(argv):
        print(f'USAGE: {argv[0]} <command> [<key>=<value>]*')
    
    @staticmethod    
    def convertKeywordValueToParameters(kwargs):
        names, strings   = [], []        
        for kwa in kwargs:
            n, s = kwa.split("=")
            names.append(n)
            strings.append(s)    
        if len(names) != len(strings):
            raise ValueError
        return names, strings
    
    @staticmethod
    def validate_arg_names(f, actual_arg_names):
        expected_arg_names = f.__code__.co_varnames[:f.__code__.co_argcount]
        if (len(actual_arg_names) != len(expected_arg_names)):
            raise ValueError        
        for expected, actual in zip(actual_arg_names, expected_arg_names):
            if expected != actual:
                raise ValueError
        
    def main(self):
        import sys
        argv = sys.argv
        
        # If not enough arguments
        if 1 >= len(argv):
            CommandLineInterface.info(argv)            
            sys.exit(1)
    
        try:
            file, comnd_name, *kwargs = argv
            
            arg_names, arg_strings = \
                CommandLineInterface.convertKeywordValueToParameters(kwargs)
            
            comnd_func = getattr(self, comnd_name)
            
            CommandLineInterface.validate_arg_names(comnd_func, arg_names)
                        
        except Exception as e:
            CommandLineInterface.info(argv)
            sys.exit(1)
        
        return_value = 0        
        try:
            return_value = comnd_func(*arg_strings)            
            sys.exit(return_value)
        except Exception as e:
            sys.exit(return_value)
        