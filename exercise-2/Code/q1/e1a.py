from pathlib import Path

def file_sizes():
    return { x.name : x.stat().st_size for x in Path('.').glob('**/*') if x.is_file() }   

if __name__ == '__main__':
    import sys
    print(file_sizes())
    sys.exit()
