from hypothesis import given, strategies as st
import json


def json_encode(x) -> str:
    """
    JSON encoder that supports only lists and numbers.
    """
    if isinstance(x, list):
        return '[' + ','.join(json_encode(ch) for ch in x) + ']'
    return str(x)


def test_json_encode():
    assert json_encode([]) == '[]'
    assert json_encode([1, 2, 3]) == '[1,2,3]'
    assert json_encode([1, [2, 3], 4]) == '[1,[2,3],4]'


# @given(x=st.lists(st.floats()))
# def test_json_encode_roundtrip(x):
#     json_string = json_encode(x)
#     assert json.loads(json_string) == x
