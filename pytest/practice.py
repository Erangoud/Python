import pytest 

def fun (x):
    return x+5 

def test_fun():
    assert fun(5) == 10 