import pyproj

def test_factorial_handles_zero():
    assert pyproj.factorial(0) == 1


def test_factorial_handles_one():
    assert pyproj.factorial(1) == 1


def test_factorial_handles_negative():
    assert pyproj.factorial(-1) == 1


def test_factorial_handles_two_through_ten():
    expected = [1, 1, 2, 6, 24, 120, 720, 5040,
                40320, 362880, 3628800]
    assert expected == [pyproj.factorial(i) for i in range(11)]
