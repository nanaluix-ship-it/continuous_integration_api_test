"""Набор тестов для проверки HTTP-запросов к postman-echo."""
import pytest

from src.echo import get_echo_data, get_echo_with_params, post_simple, post_form_data


@pytest.mark.get
def test_get_none_param():
    """Тестирование GET запроса без параметров"""
    data = get_echo_data()
    assert isinstance(data, dict)
    assert "headers" in data

@pytest.mark.get_list
def test_get_with_list(list_query_data):
    """Тестирование GET запроса списком параметров"""
    response = get_echo_with_params(list_query_data)
    assert isinstance(response, dict)
    args = response["args"]
    assert args["page"] == "2"
    assert "tags" in args
    assert isinstance(args["tags"], list)


@pytest.mark.get_params
def test_parameters_are_sent(sample_params):
    """Проверяет передачу параметров через query-строку"""
    response = get_echo_with_params(sample_params)
    assert isinstance(response, dict)
    assert "name" in response["args"]
    assert "age" in response["args"]
    assert "city" in response["args"]


@pytest.mark.post
def test_post_simple(sample_json_payload):
    """Тестирование POST запроса"""
    response = post_simple(sample_json_payload)
    assert isinstance(response, dict)
    assert response["json"]["id"] == 777
    assert response["json"]["is_new"] is True
    assert response["json"]["message"] == "Hello, is POST"


@pytest.mark.post_form
def test_post_form(sample_form_payload):
    """Тестирование POST запроса с формой"""
    response = post_form_data(sample_form_payload)
    assert isinstance(response, dict)
    server_form = response["form"]
    assert server_form["username"] == "tester"
    assert server_form["password"] == "secret123"
