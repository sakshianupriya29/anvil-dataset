from solution import allow_request, user_requests

def reset():
    user_requests.clear()

def test_basic_allow():
    reset()
    assert allow_request("u1", 1) == True

def test_limit_exceeded():
    reset()
    allow_request("u1", 1)
    allow_request("u1", 2)
    allow_request("u1", 3)
    assert allow_request("u1", 4) == False

def test_reset_after_time():
    reset()
    allow_request("u1", 1)
    allow_request("u1", 2)
    allow_request("u1", 3)
    assert allow_request("u1", 6) == True

def test_multiple_users():
    reset()
    allow_request("u1", 1)
    allow_request("u1", 2)
    allow_request("u1", 3)
    assert allow_request("u2", 1) == True

def test_exact_boundary():
    reset()
    allow_request("u1", 1)
    allow_request("u1", 2)
    allow_request("u1", 3)
    assert allow_request("u1", 6) == True

def test_independent_tracking():
    reset()
    allow_request("u1", 1)
    allow_request("u2", 1)
    allow_request("u1", 2)
    allow_request("u2", 2)
    assert allow_request("u1", 3) == True