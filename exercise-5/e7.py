import os
from pathlib import Path
import pytest
import shutil
from simple import read_value, write_value
import tempfile

@pytest.fixture
def path():
    temp_path = Path(tempfile.mkdtemp())
    
    def write_to_file(path, fname, data):
        with open(path / fname, 'w') as file:
            file.write(str(data))            
    
    write_to_file(temp_path, 'n.txt', 1)
    write_to_file(temp_path, 's.txt', "\'Hello, world!\'")
    write_to_file(temp_path, 'l.txt', [1, 2, 3, 4, 5])
        
    try:
        yield temp_path
    finally:
        shutil.rmtree(temp_path)
    

def test_read_values(path):
    n = path / 'n.txt'
    assert read_value(n) == 1
    s = path / 's.txt'
    assert read_value(s) == 'Hello, world!'
    l = path / 'l.txt'
    assert read_value(l) == [1, 2, 3, 4, 5]
