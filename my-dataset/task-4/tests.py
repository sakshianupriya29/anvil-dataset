from solution import add_number, window

def reset():
    window.clear()

def test_first():
    reset()
    assert add_number(1) == 1.0

def test_two_numbers():
    reset()
    add_number(1)
    assert add_number(2) == 1.5

def test_three_numbers():
    reset()
    add_number(1)
    add_number(2)
    assert add_number(3) == 2.0

def test_sliding_window():
    reset()
    add_number(1)
    add_number(2)
    add_number(3)
    assert add_number(4) == 3.0

def test_window_size():
    reset()
    add_number(1)
    add_number(2)
    add_number(3)
    add_number(4)
    assert len(window) == 3

def test_continuous():
    reset()
    add_number(1)
    add_number(2)
    add_number(3)
    add_number(4)
    assert add_number(5) == 4.0