from dataclasses import dataclass
from hypothesis import given, strategies as st

# https://hypothesis.readthedocs.io/en/latest/data.html


@dataclass
class UserModel:
    username: str
    email: str
    ip_address: str


@given(
    st.builds(
        UserModel,
        username=st.text(),
        email=st.emails(),
        ip_address=st.ip_addresses(),
    )
)
def test_generated(obj):
    print('!!!', obj)
