import pytest

from src.echo import get_echo_data, get_echo_with_params, post_simple


@pytest.mark.get
def test_get_none_param():
    data = get_echo_data()
    assert "headers" in data

@pytest.mark.get_params
def test_parameters_are_sent():
    sent_data = {
        "name": "Alice",
        "age": 30,
        "city": "Moscow"
    }
    response = get_echo_with_params(sent_data)

    assert "name" in response["args"]
    assert "age" in response["args"]
    assert "city" in response["args"]


@pytest.mark.post
def test_post_simple():
    # Готовим данные: числа остаются числами, булевы — булевыми
    my_data = {
        "id": 777,
        "is_new": True,
        "message": "Hello, is POST"
    }
    response = post_simple(my_data)

    assert response["json"]["id"] == 777
    assert response["json"]["is_new"] is True
    assert response["json"]["message"] == "Hello, is POST"