
class TypedProperty:
    _TYPED_PROPERTY_NAME_POSTFIX_    = '_TYPED_PROPERTY'
    
    @staticmethod
    def _toTypedPropertyName(name):
        return name + TypedProperty._TYPED_PROPERTY_NAME_POSTFIX_
    
    def __init__(self, type):
        self.property_type = type

    def __set__(self, instance, value):         
        if not isinstance(value, self.property_type):
            raise ValueError(f'attribute {self.name!r} must be {self.property_type}')
        if self.name in instance.__dict__:
            instance.__dict__[self.name] = value
        else:
            setattr(instance.__class__, TypedProperty._toTypedPropertyName(self.name), value)

    def __get__(self, instance, cls): 
        if instance is None:
            return cls.__dict__[self.name]            
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]       
        else:
            return getattr(instance.__class__, TypedProperty._toTypedPropertyName(self.name))
    
    def __delete__(self, instance):
        instance.__dict__[self.name] = self.property_type()

    def __set_name__(self, cls, name):
        self.name = name
        setattr(cls, TypedProperty._toTypedPropertyName(self.name), self.property_type())
        