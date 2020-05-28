from pathlib import Path

class CEntry:
    def __init__(self, path):
        self.name       = path.name
        self.is_skip    = False
        self.type       = 'other'
        
        if Path.is_file(path):
            self.type = 'file'
        elif Path.is_dir(path):
            self.type = 'directory'
            
    def skip(self):
        self.is_skip = True
    
def walk(root):
    path = Path(root)
    # Taking subitems
    current_dir_items = [p for p in path.iterdir()]
    # Sorting alphabetically by their name.    
    current_dir_items.sort(key=lambda x: x.name)
    scan_sub_dir_items = []
    # Yielding top items
    for c in current_dir_items:
        e = CEntry(c)
        yield e
        if not e.is_skip:
            scan_sub_dir_items.append(c)        
    # Going over the sub-items in a breadth-first search matter 
    for s in scan_sub_dir_items:
        if Path.is_dir(s):
            yield from walk(s)
    
def fs(tmp_path):
    d1 = tmp_path / 'd1'
    d1.mkdir()
    f1 = tmp_path / 'f1'
    f1.write_text('1')
    d2 = d1 / 'd2'
    d2.mkdir()
    f2 = d1 / 'f2'
    f2.write_text('2')
    d3 = d2 / 'd3'
    d3.mkdir()
    d4 = d2 / 'd4'
    d4.mkdir()
    f3 = d3 / 'f3'
    f3.write_text('3')
    return tmp_path

def main():
    tmp_path = Path("tmp")
    root = tmp_path
    if not tmp_path.exists():
        tmp_path.mkdir()
        root = fs(tmp_path)
    
    for e in walk(root):
        print(f'{e.name} ({e.type})')
        if e.name == 'd2':
            e.skip()

  
if __name__== "__main__":
    main()

