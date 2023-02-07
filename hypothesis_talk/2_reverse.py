from hypothesis import given, strategies as st


def reverse_list(xs: list[int]):
    # result = xs[::-1]

    result = []
    pos = len(xs) - 1
    while pos:
        result.append(xs[pos])
        pos -= 1
    result.append(xs[0])

    return result


def test_reverse_list():
    assert reverse_list([1, 2, 3]) == [3, 2, 1]
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]


# @given(xs=st.lists(st.integers()))
# def test_reverse_list_roundtrip(xs):
#     assert reverse_list(reverse_list(xs)) == xs
