from solution import can_request, last_request_time

def reset():
    last_request_time.clear()

def test_first_request():
    reset()
    assert can_request("u1", 1) == True

def test_block_within_time():
    reset()
    can_request("u1", 1)
    assert can_request("u1", 3) == False

def test_allow_after_5_seconds():
    reset()
    can_request("u1", 1)
    assert can_request("u1", 6) == True

def test_exact_boundary():
    reset()
    can_request("u1", 1)
    assert can_request("u1", 6) == True

def test_multiple_users():
    reset()
    can_request("u1", 1)
    assert can_request("u2", 2) == True

def test_update_time():
    reset()
    can_request("u1", 1)
    can_request("u1", 6)
    assert can_request("u1", 8) == False