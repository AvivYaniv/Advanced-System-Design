import math
import pytest
from simple import mul, div, greet, write_value, read_value

def test_mul():
    """
    check that mul performs multiplication well on 
    positive integers
    """
    # Checking on the 'multiplicative identity'
    assert mul(1,2)             == 2
    assert mul(5,1)             == 5
    
    # Sanity check
    assert mul(2,3)             == 6
    
    # Sanity check of commutativity
    assert mul(7,9)             == mul(9,7)
    
    # Sanity check on numbers above 100, 1000
    assert mul(125,9)           ==  1125
    assert mul(8,5847)          ==  46776


def test_mul_zero():
    """
    check that mul performs multiplication well on 
    zero and 
    other numbers.
    """
    # Sanity check on small positive numbers 
    assert mul(0,2)             == 0
    assert mul(5,0)             == 0
    
    # Sanity check on small negative numbers
    assert mul(0,-3)            == 0
    assert mul(-7,0)            == 0
    
    # Sanity check on positive numbers above 100, 1000
    assert mul(125,0)           ==  0
    assert mul(0,5847)          ==  0

    # Sanity check on negative numbers above 100, 1000
    assert mul(-125,0)          ==  0
    assert mul(0,-5847)         ==  0

def test_mul_negative():
    """
    Check that mul performs multiplication well on 
    a negative number and 
    other numbers, and on 
    two negative numbers.
    """
    # Checking on the 'multiplicative identity'
    assert mul(1,-2)            == -2
    assert mul(-5, 1)           == -5
    
    # Checking on the negative of 'multiplicative identity'
    assert mul(-1,2)            == -2
    assert mul(5,-1)            == -5
    
    # Sanity check on two small negative numbers
    assert mul(-2,-3)           == 6
    assert mul(-2,-3)           == 6
    
    # Sanity check of commutativity
    assert mul(7,-9)            == mul(-7,9)
    assert mul(-7,-9)           == mul(7,9)
    
    # Sanity check on negative numbers above 100, 1000
    assert mul(125,-9)          ==  -1125
    assert mul(-125,-9)         ==  1125
    assert mul(-125,9)          ==  -1125
    assert mul(-8,5847)         ==  -46776
    assert mul(-8,-5847)        ==  46776
    assert mul(8,-5847)         ==  -46776


def test_mul_fraction():
    """
    Check that mul performs multiplication well on a 
    fraction and 
    other numbers
    """
    # Checking on multiplicative inverse, finite decimal representation parameters
    assert mul(0.5,-2)          == -1
    assert mul(-0.5,2)          == -1
    assert mul(0.5,2)           == 1
    assert mul(-0.5,-2)         == 1
    
    # Checking on multiplicative inverse, infinite decimal representation parameters
    assert mul(-1/3.0,3)        == -1.0
    assert mul(3, -1/3.0)       == -1.0
    assert mul(1/3.0,-3)        == -1.0
    assert mul(-3, 1/3.0)       == -1.0    
    assert mul(-1/3.0,-3)       == 1.0
    assert mul(-3, -1/3.0)      == 1.0
    assert mul(1/3.0,3)         == 1.0
    assert mul(3, 1/3.0)        == 1.0
    
    # Checking on finite decimal representation parameters
    assert mul(0.25,-2)         == -0.5
    assert mul(-0.25,2)         == -0.5
    assert mul(0.25,2)          == 0.5
    assert mul(-0.25,-2)        == 0.5
    
    # Checking on infinite decimal representation parameters
    assert math.isclose(mul(2/7.0,5.0), 10/7.0)
    assert math.isclose(mul(3.0, 2/9.0), 6/9.0)
    assert math.isclose(mul(-2/7.0,-5.0), 10/7.0)
    assert math.isclose(mul(-3.0, -2/9.0), 6/9.0)
    assert math.isclose(mul(-2/7.0,5.0), -10/7.0)
    assert math.isclose(mul(-3.0, 2/9.0), -6/9.0)
    assert math.isclose(mul(2/7.0,-5.0), -10/7.0)
    assert math.isclose(mul(3.0, -2/9.0), -6/9.0)

def test_div():
    """
    check that div performs division well on 
    positive integers.
    """
    # Checking on the 'multiplicative identity'
    assert div(2,1)             == 2
    assert div(2,2)             == 1
    assert div(5,5)             == 1
    assert div(5,1)             == 5
    
    # Sanity check
    assert div(6,2)             == 3
        
    # Sanity check on numbers above 100, 1000
    assert div(1125,125)        == 9
    assert div(1125,9)          == 125
    assert div(46776,8)         == 5847
    assert div(46776,5847)      == 8

def test_div_negative():
    """
    Check that div performs division well on a 
    negative number and 
    other numbers, and on 
    two negative numbers.
    """
    # Checking on the 'multiplicative identity'
    assert div(-2,1)            == -2
    assert div(-2,-2)           == 1
    assert div(-5,-5)           ==  1
    assert div(-5, 1)           == -5
    
    # Checking on the negative of 'multiplicative identity'
    assert div(-2,-1)           == 2
    assert div(-2,2)            == -1
    assert div(-5,5)            == -1
    assert div(-5,-1)           == 5
    
    # Sanity check on two small negative numbers
    assert div(6,-2)            == -3
    assert div(6,-3)            == -2
    assert div(-6,-2)           == 3
    assert div(-6,-3)           == 2
        
    # Sanity check on negative numbers above 100, 1000
    assert div(-1125,125)       == -9
    assert div(-1125,-9)        == 125
    assert div(1125,-125)       == -9
    assert div(1125,-9)         == -125
    assert div(-1125,-125)      == 9
    assert div(-1125,9)         == -125
    assert div(-46776,-8)       == 5847
    assert div(-46776,5847)     == -8
    assert div(46776,-8)        == -5847
    assert div(46776,-5847)     == -8
    assert div(-46776,8)        == -5847
    assert div(-46776,-5847)    == 8


def test_div_fraction():
    """
    Check that div performs division well on a 
    fraction and 
    other numbers
    """    
    # Checking on multiplicative inverse, finite decimal representation parameters
    assert div(-1,0.5)          == -2
    assert div(-1,-0.5)         == 2
    assert div(1,0.5)           == 2
    assert div(1,-0.5)          == -2
    
    # Checking on multiplicative inverse, infinite decimal representation parameters
    assert div(-1.0,-1/3.0)     == 3
    assert div(-1.0, -1/3.0)    == 3
    assert div(-1.0,1/3.0)      == -3
    assert div(-1.0, 1/3.0)     == -3
    assert div(1.0,-1/3.0)      == -3
    assert div(1.0, -1/3.0)     == -3
    assert div(1.0,1/3.0)       == 3
    assert div(1.0, 1/3.0)      == 3
    
    # Checking on finite decimal representation parameters
    assert div(-0.5,0.25)       == -2
    assert div(-0.5,-2)         == 0.25
    assert div(-0.5,-0.25)      == 2
    assert div(-0.5,2)          == -0.25
    assert div(0.5,0.25)        == 2
    assert div(0.5,2)           == 0.25
    assert div(0.5,-0.25)       == -2
    assert div(0.5,-2)          == -0.25
    
    # Checking on infinite decimal representation parameters
    assert math.isclose(div(10/7.0,2/7.0), 5.0)
    assert math.isclose(div(10/7.0,5.0), 2/7.0)
    assert math.isclose(div(6/9.0,3.0),  2/9.0)
    assert math.isclose(div(6/9.0, 2/9.0), 3.0)
    assert math.isclose(div(10/7.0,-2/7.0), -5.0)
    assert math.isclose(div(10/7.0,-5.0), -2/7.0)
    assert math.isclose(div(6/9.0,-3.0),  -2/9.0)
    assert math.isclose(div(6/9.0, -2/9.0), -3.0)
    assert math.isclose(div(-10/7.0,-2/7.0), 5.0)
    assert math.isclose(div(-10/7.0,5.0), -2/7.0)
    assert math.isclose(div(-6/9.0,-3.0),  2/9.0)
    assert math.isclose(div(-6/9.0, 2/9.0), -3.0)
    assert math.isclose(div(-10/7.0,2/7.0), -5.0)
    assert math.isclose(div(-10/7.0,-5.0), 2/7.0)
    assert math.isclose(div(-6/9.0,3.0),  -2/9.0)
    assert math.isclose(div(-6/9.0, -2/9.0), 3.0)


def test_div_error():
    """
    Check that div raises a ZeroDivisionError when dividing by zero
    """
    # Sanity check on small positive numbers 
    with pytest.raises(ZeroDivisionError):
        assert div(0,0)
    
    with pytest.raises(ZeroDivisionError):
        assert div(5,0)
    
    # Sanity check on small negative numbers
    with pytest.raises(ZeroDivisionError):
        assert div(-3,0)
    
    with pytest.raises(ZeroDivisionError):
        assert div(-7,0)
    
    # Sanity check on positive numbers above 100, 1000
    with pytest.raises(ZeroDivisionError):
        assert div(125,0)
    
    with pytest.raises(ZeroDivisionError):
        assert div(5847,0)
    
    # Sanity check on negative numbers above 100, 1000
    with pytest.raises(ZeroDivisionError):
        assert div(-125,0)
    
    with pytest.raises(ZeroDivisionError):
        assert div(-5847,0)

def test_greet(capsys):
    """
    Check that greet(name) prints a hello message to the name provided to it
    """
    name = 'Agat'
    greet(name)
    stdout, stderr = capsys.readouterr()
    
    assert stdout == f'Hello, {name}!\n'
    assert stderr == ''


def test_greet_stranger(capsys):
    """
    Check that greet() prints a hello message to a stranger if no name is provided to it
    """
    greet(None)
    stdout, stderr = capsys.readouterr()
    
    assert stdout == 'Hello, stranger!\n'
    assert stderr == ''


def test_read_value_int(tmp_path):
    """
    Check that read_value can successfully 
    read the integers 
    1 and 
    2 
    from a file 
    (use write_value to write it there)
    """
    f = tmp_path / 'file.txt'
    write_value(f, 1)
    assert read_value(str(f)) == 1
    
    f = tmp_path / 'file.txt'
    write_value(f, 2)
    assert read_value(str(f)) == 2

def test_read_value_str(tmp_path):
    """
    Check that read_value can successfully 
    read the strings 
    foo and 
    bar 
    from a file 
    (use write_value to write it there)
    """
    f = tmp_path / 'file.txt'
    write_value(f, 'foo')
    assert read_value(str(f)) == 'foo'
    
    f = tmp_path / 'file.txt'
    write_value(f, 'bar')
    assert read_value(str(f)) == 'bar'


def test_read_value_list(tmp_path):
    """
    Check that read_value can successfully 
    read the lists 
    [1, 2, 3] and 
    [] 
    from a file 
    (use write_value to write it there)
    """
    f = tmp_path / 'file.txt'
    write_value(f, [1, 2, 3])
    assert read_value(str(f)) == [1, 2, 3]
    
    f = tmp_path / 'file.txt'
    write_value(f, [])
    assert read_value(str(f)) == []
