import pytest
from cqd import cqd


class TestClass:
    def __init__(self):
        self.public_attr = 1
        self._protected_attr = 2


def test_cqd_function(capsys):
    obj = TestClass()
    cqd(obj)
    captured = capsys.readouterr()
    assert "__init__" in captured.out
    assert "_protected_attr" in captured.out
    assert "public_attr" in captured.out