from simpleintrest import simple_interest

def test_interest1():
    assert simple_interest(1000, 5, 2) == 100

def test_interest2():
    assert simple_interest(2000, 10, 3) == 600