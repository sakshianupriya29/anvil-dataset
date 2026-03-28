from solution import visit, daily_users

def reset():
    daily_users.clear()
    global current_day
    current_day = None

def test_first_visit():
    reset()
    assert visit("u1", 1) == 1

def test_unique_users():
    reset()
    visit("u1", 1)
    assert visit("u2", 1) == 2

def test_duplicate_visit():
    reset()
    visit("u1", 1)
    assert visit("u1", 1) == 1

def test_new_day_reset():
    reset()
    visit("u1", 1)
    assert visit("u2", 2) == 1

def test_multiple_users_same_day():
    reset()
    visit("u1", 1)
    visit("u2", 1)
    visit("u3", 1)
    assert visit("u4", 1) == 4

def test_reset_then_add():
    reset()
    visit("u1", 1)
    visit("u2", 1)
    visit("u3", 2)
    assert visit("u4", 2) == 2