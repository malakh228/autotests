import pytest
from pygments.styles.dracula import yellow


@pytest.fixture()
def before_after():
    print('before test')
    yield
    print('\nAfter test')




def test_demo1():
    assert 1 == 1

def test_demo2(before_after):
        assert 2 == 3