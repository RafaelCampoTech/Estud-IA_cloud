import pytest

from function import dummy_function
from main import main


def test_main_prints_greeting(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from simple-fastapi!\n"


def test_dummy_function_default_returns_greeting():
    assert dummy_function() == "Hello from dummy_function!"


def test_dummy_function_explicit_dummy_returns_greeting():
    assert dummy_function("Dummy") == "Hello from dummy_function!"


def test_dummy_function_other_value_raises():
    with pytest.raises(ValueError, match="a is not Dummy"):
        dummy_function("other")
