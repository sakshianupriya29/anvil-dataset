from solution import login, fail_count, lock_time

def reset():
    fail_count.clear()
    lock_time.clear()

def test_success():
    reset()
    assert login("u1", True, 1) == "SUCCESS"

def test_fail_attempts():
    reset()
    assert login("u1", False, 1) == "FAIL"
    assert login("u1", False, 2) == "FAIL"

def test_lock_after_3_fails():
    reset()
    login("u1", False, 1)
    login("u1", False, 2)
    assert login("u1", False, 3) == "LOCKED"

def test_locked_state():
    reset()
    login("u1", False, 1)
    login("u1", False, 2)
    login("u1", False, 3)
    assert login("u1", True, 5) == "LOCKED"

def test_unlock_after_time():
    reset()
    login("u1", False, 1)
    login("u1", False, 2)
    login("u1", False, 3)
    assert login("u1", True, 15) == "SUCCESS"

def test_multiple_users():
    reset()
    login("u1", False, 1)
    login("u2", False, 1)
    login("u1", False, 2)
    login("u2", False, 2)
    assert login("u2", False, 3) == "LOCKED"