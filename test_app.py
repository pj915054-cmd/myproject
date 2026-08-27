from app import add,subtract,mutiple,divide

def test_add():
    assert add(10, 20) == 30

def test_subtract():
    assert subtract(10,20) == -10

def test_mutiple():
    assert mutiple(10,20) == 300

def test_divide():
    assert divide(10,20) == 0
    
