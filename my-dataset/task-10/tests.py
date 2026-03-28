import solution

def reset():
    solution.url_to_code.clear()
    solution.code_to_url.clear()
    solution.counter = 1

def test_shorten():
    reset()
    assert solution.shorten("a.com") == "1"

def test_multiple_urls():
    reset()
    solution.shorten("a.com")
    assert solution.shorten("b.com") == "2"

def test_same_url():
    reset()
    solution.shorten("a.com")
    assert solution.shorten("a.com") == "1"

def test_resolve():
    reset()
    solution.shorten("a.com")
    assert solution.resolve("1") == "a.com"

def test_invalid_code():
    reset()
    assert solution.resolve("99") == None

def test_sequence():
    reset()
    solution.shorten("a.com")
    solution.shorten("b.com")
    assert solution.resolve("2") == "b.com"