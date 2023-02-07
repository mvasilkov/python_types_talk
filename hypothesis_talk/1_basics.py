from hypothesis import given, strategies as st


def is_nonnegative_integer(x: float):
    # return x.is_integer() and x >= 0

    x_string = str(x)
    if x_string.startswith('-'):
        return False
    if not x_string.endswith('.0'):
        return False
    return True


def test_is_nonnegative_integer():
    assert is_nonnegative_integer(0.0)
    assert is_nonnegative_integer(1.0)
    assert not is_nonnegative_integer(-1.0)
    assert not is_nonnegative_integer(1.1)
    assert not is_nonnegative_integer(-1.1)


# @given(x=st.floats())
# def test_nonnegative_hypothesis(x):
#     expected = x.is_integer() and x >= 0
#     assert is_nonnegative_integer(x) == expected
