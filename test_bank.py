from bank import value

def test_default():
    assert value("hello, you!") == 0

def test_capital_default():
    assert value("Hello, you!") == cs0

def test_h():
    assert value("hi, you!") == 20

def test_capital_h():
    assert value("Hi, you!") == 20

def test_any_other_word():
    assert value("I just woke up") == 100

def test_numbers():
    assert value("1234") == 100

def test_punctuation():
    assert value(",!.") == 100
