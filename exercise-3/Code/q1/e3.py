class TransformDict:
    def __init__(self, transform_function):
        self.dictionary = dict()
        self.transform_function = transform_function

    def __setitem__(self, key, item):
        self.dictionary[self.transform_function(key)] = item

    def __getitem__(self, key):
        if isinstance(key, int):
            i = key
            return list(self.dictionary.keys())[i]
        else:
            return self.dictionary[self.transform_function(key)]

    def __repr__(self):
        return self.dictionary.__repr__()

    def __len__(self):
        return len(self.dictionary)

    def __delitem__(self, key):
        del self.dictionary[self.transform_function(key)]
        
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return 0 == len(set(self.dictionary.items()) ^ set(other.dictionary.items()))

    def __bool__(self):
        return 0 != len(self.dictionary.items())

    def __hash__(self):
        return hash(self.dictionary)

    def clear(self):
        return self.dictionary.clear()

    def copy(self):
        return self.dictionary.copy()

    def __contains__(self, key):
        return self.transform_function(key) in self.dictionary

    def update(self, *args, **kwargs):
        return self.dictionary.update(*args, **kwargs)

    def keys(self):
        return self.dictionary.keys()

    def values(self):
        return self.dictionary.values()
    
def main():
    d = TransformDict(lambda key: key.lower())
    d['x'] = 1
    d['y'] = 2
    print(list(d))
  
if __name__== "__main__":
    main()
    