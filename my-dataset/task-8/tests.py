from solution import add_task, get_next_task, tasks

def reset():
    tasks.clear()

def test_basic():
    reset()
    add_task("t1", 1)
    assert get_next_task(2) == "t1"

def test_fifo():
    reset()
    add_task("t1", 1)
    add_task("t2", 2)
    assert get_next_task(3) == "t1"
    assert get_next_task(4) == "t2"

def test_expiry():
    reset()
    add_task("t1", 1)
    assert get_next_task(15) == None

def test_skip_expired():
    reset()
    add_task("t1", 1)
    add_task("t2", 2)
    assert get_next_task(15) == None

def test_mixed():
    reset()
    add_task("t1", 1)
    add_task("t2", 5)
    assert get_next_task(12) == "t2"

def test_empty():
    reset()
    assert get_next_task(5) == None