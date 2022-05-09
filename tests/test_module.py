import pytest
from my_library.my_module import my_function


def test_module():
    assert my_function() == 42
