import inspect

class FunctionsList(list):
    pass

class OverloadedMethodsDict(dict):
    def __setitem__(self, name, value):
        if name not in self or not callable(value):
            super().__setitem__(name, value)
        else:
            current_function = value
            function_name_mapped_value = self[name]
            # If name mapped by function
            if callable(function_name_mapped_value):
                # Create list containing function
                overloaded_methods_list = FunctionsList([function_name_mapped_value])
            # Else, if name mapped by function list
            elif isinstance(function_name_mapped_value, FunctionsList):
                overloaded_methods_list = function_name_mapped_value
            # Appending current function to methods list
            overloaded_methods_list.append(current_function) 
            # Setting under name the function list
            super().__setitem__(name, overloaded_methods_list)

class Overloaded(type):
    @classmethod
    def __prepare__(cls, clsname, bases):
        return OverloadedMethodsDict()

    def __new__(cls, name, bases, attrs):
        obj = super().__new__(cls, name, bases, attrs)
        
        # Going over all items defined in class
        for name, value in attrs.items():
            # If not function list, continue
            if not isinstance(value, FunctionsList):
                continue
            # Else, arrived here - adding a function that binds all overloads
            def unified_overloads_function(self, *args, **kwargs):
                overloaded_methods_list = value
                # Going over all overloads and trying to call each one of them
                for method in overloaded_methods_list:
                    try:
                        return method(self, *args, **kwargs)
                    except TypeError:
                        continue
            # Setting the unified overloads functions to be called upon 'name' function
            setattr(obj, name, unified_overloads_function)
        return obj
    