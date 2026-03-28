from solution import search, history

def reset():
    history.clear()

def test_first_search():
    reset()
    assert search("u1", "a") == ["a"]

def test_order():
    reset()
    search("u1", "a")
    assert search("u1", "b") == ["b", "a"]

def test_duplicate_move():
    reset()
    search("u1", "a")
    search("u1", "b")
    assert search("u1", "a") == ["a", "b"]

def test_limit():
    reset()
    for i in ["a","b","c","d","e","f"]:
        search("u1", i)
    assert len(search("u1", "g")) == 5

def test_no_duplicates():
    reset()
    search("u1", "a")
    search("u1", "a")
    assert search("u1", "a") == ["a"]

def test_multiple_users():
    reset()
    search("u1", "a")
    search("u2", "b")
    assert search("u2", "c") == ["c", "b"]