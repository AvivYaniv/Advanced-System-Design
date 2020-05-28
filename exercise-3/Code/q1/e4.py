
class MultiDict:
    def __init__(self):
        self.dictionary = dict()

    def __setitem__(self, key, item):
        if key not in self.dictionary.keys():
            self.dictionary[key] = [item]
        else:
            self.dictionary[key].append(item)

    def __getitem__(self, i):
        if isinstance(i, int):
            return list(self.dictionary.keys())[i]
        else:
            if i not in self.dictionary.keys():
                raise KeyError
            return self.dictionary[i][0]

    def get_all(self, key):
        if key not in self.dictionary.keys():
            raise KeyError
        return self.dictionary[key]
        
    def __repr__(self):
        return self.dictionary.__repr__()

    def __len__(self):
        return len(self.dictionary)
    
    def __delitem__(self, key):
        if key not in self.dictionary.keys():
            raise KeyError
        else:
            self.dictionary[key].pop(0)
            if 0 == len(self.dictionary[key]):
                del self.dictionary[key]

    def delete_all(self, key):
        if key not in self.dictionary.keys():
            raise KeyError        
        del self.dictionary[key]
        
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return len(self.dictionary) == \
            len({k: self.dictionary[k] \
                 for k in self.dictionary \
                 if k in other.dictionary and self.dictionary[k] == other.dictionary[k]})

    def __bool__(self):
        return 0 != len(self.dictionary.items())

    def __hash__(self):
        return hash(self.dictionary)

    def clear(self):
        return self.dictionary.clear()

    def copy(self):
        return self.dictionary.copy()

    def __contains__(self, key):
        return key in self.dictionary
    
    def update(self, *args, **kwargs):
        return self.dictionary.update(*args, **kwargs)

    def keys(self):
        return self.dictionary.keys()

    def values(self):
        return self.dictionary.values()
    
def main():
    d = MultiDict()
    d['x'] = 1
    d['y'] = 2
    print(list(d))
  
if __name__== "__main__":
    main()
