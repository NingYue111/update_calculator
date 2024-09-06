from calculator import abs

def test_abs():
    results = abs(-5)
    assert results == 5

    results = abs(3)
    assert results == 3

