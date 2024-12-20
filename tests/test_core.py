import pytest
from cqd import cqd, cqd2


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


def test_cqd2_function(capsys):
    obj = TestClass()
    cqd2(obj)
    captured = capsys.readouterr()
    assert "__init__" in captured.out
    assert "_protected_attr" in captured.out
    assert "public_attr" in captured.out
    assert "int" in captured.out
