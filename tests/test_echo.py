import pytest

from src.echo import get_echo_data, get_echo_with_params

@pytest.mark.get
def test_get_none_param():
    data = get_echo_data()
    assert "headers" in data

@pytest.mark.get_params
def test_parameters_are_sent():
    sent_data = {"name": "Alice", "age": 30, "city": "Moscow"} # Числа остаются числами!
    response = get_echo_with_params(sent_data)

    assert "name" in response["args"]
    assert "age" in response["args"]
    assert "city" in response["args"]