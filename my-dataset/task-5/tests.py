from solution import send_notification, get_next_notification, queues

def reset():
    queues.clear()

def test_single_notification():
    reset()
    send_notification("u1", "Hello")
    assert get_next_notification("u1") == "Hello"

def test_fifo_order():
    reset()
    send_notification("u1", "A")
    send_notification("u1", "B")
    assert get_next_notification("u1") == "A"
    assert get_next_notification("u1") == "B"

def test_empty_queue():
    reset()
    assert get_next_notification("u1") == None

def test_multiple_users():
    reset()
    send_notification("u1", "A")
    send_notification("u2", "B")
    assert get_next_notification("u2") == "B"
    assert get_next_notification("u1") == "A"

def test_removal_after_fetch():
    reset()
    send_notification("u1", "A")
    get_next_notification("u1")
    assert get_next_notification("u1") == None

def test_multiple_messages():
    reset()
    send_notification("u1", "A")
    send_notification("u1", "B")
    send_notification("u1", "C")
    assert get_next_notification("u1") == "A"