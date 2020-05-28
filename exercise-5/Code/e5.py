import sys

class MagicModule:
    def __call__(self, x):
        return x
    
    def __getitem__(self, x):
        return x
    
    def __repr__(self):
        return 'magic module'

sys.modules[__name__] = MagicModule()
