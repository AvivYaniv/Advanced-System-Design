import numbers

class LazyExpression:
    def __init__(self, expr):
        self.expr   = expr
        
    def __repr__(self):
        return self.expr

    def evaluate(self, **kwargs):
        evaluate_expression = self.expr
        for key, value in kwargs.items(): 
            # If value not integer
            if not isinstance(value, numbers.Number):
                raise ValueError
            # Replacing key with value
            evaluate_expression = \
                evaluate_expression.replace(key, str(value))
        return eval(evaluate_expression)
    
    def __left_operator__(self, other, sign):
        result = LazyExpression(self.expr)
        result.expr = \
            '(' + result.expr + ' ' + sign + ' ' + str(other) + ')'
        return result
    
    def __right_operator__(self, other, sign):
        result = LazyExpression(self.expr)
        result.expr = \
            '(' + str(other) + ' ' + sign + ' ' + result.expr + ')'
        return result
        
    def __add__(self, other): 
        return self.__left_operator__(other, '+')
    
    def __radd__(self, other): 
        return self.__right_operator__(other, '+')
    
    def __sub__(self, other): 
        return self.__left_operator__(other, '-')
    
    def __rsub__(self, other): 
        return self.__right_operator__(other, '-')

    def __mul__(self, other): 
        return self.__left_operator__(other, '*')
    
    def __rmul__(self, other): 
        return self.__right_operator__(other, '*')
    
    def __truediv__(self, other): 
        return self.__left_operator__(other, '/')
    
    def __rtruediv__(self, other): 
        return self.__right_operator__(other, '/')
    
    def __pos__(self): 
        result = LazyExpression(self.expr)
        if '+' != result.expr[0]:
            if '-' == result.expr[0]:
                result.expr = result.expr[1:]            
            result.expr = '+' + result.expr
        return result
    
    def __neg__(self): 
        result = LazyExpression(self.expr)
        if '-' != result.expr[0]:
            if '+' == result.expr[0]:
                result.expr = result.expr[1:]            
            result.expr = '-' + result.expr
        return result

class LazyVariable(LazyExpression):
    def __init__(self, v):
        self.var_name = v
        super(LazyVariable, self).__init__(v)
        