from solution import send_message, message_log

def reset():
    message_log.clear()

def test_first_message():
    reset()
    assert send_message("u1", "Hi", 1) == True

def test_duplicate_message():
    reset()
    send_message("u1", "Hi", 1)
    assert send_message("u1", "Hi", 5) == False

def test_after_10_seconds():
    reset()
    send_message("u1", "Hi", 1)
    assert send_message("u1", "Hi", 12) == True

def test_different_users():
    reset()
    send_message("u1", "Hi", 1)
    assert send_message("u2", "Hi", 2) == True

def test_case_sensitive():
    reset()
    send_message("u1", "Hi", 1)
    assert send_message("u1", "hi", 2) == True

def test_multiple_messages():
    reset()
    send_message("u1", "Hello", 1)
    send_message("u1", "Hi", 2)
    assert send_message("u1", "Hello", 5) == False