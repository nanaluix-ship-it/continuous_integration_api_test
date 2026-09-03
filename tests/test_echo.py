import pytest

from src.echo import get_echo_data, get_echo_with_params, post_simple, post_form_data


@pytest.mark.get
def test_get_none_param():
    data = get_echo_data()
    assert "headers" in data

@pytest.mark.get_list
def test_get_with_list():
    query_data = {
        "page": 2,
        "tags": ["admin", "vip", "editor"]
    }
    response = get_echo_with_params(query_data)
    args = response["args"]
    assert args["page"] == "2"
    assert "tags" in args


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
    my_data = {
        "id": 777,
        "is_new": True,
        "message": "Hello, is POST"
    }
    response = post_simple(my_data)
    assert response["json"]["id"] == 777
    assert response["json"]["is_new"] is True
    assert response["json"]["message"] == "Hello, is POST"


@pytest.mark.post_form
def test_post_form():
    form_data = {
        "username": "tester_999",
        "password": "secret123",
        "remember": "true"
    }
    response = post_form_data(form_data)
    server_form = response["form"]
    assert server_form["username"] == "tester_999"
    assert server_form["password"] == "secret123"