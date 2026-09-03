"""Фикстуры для всего набора тестов"""

import pytest

@pytest.fixture
def sample_params():
    """Словарь параметров для GET-запроса."""
    return {"name": "Alice", "age": 30, "city": "Moscow"}

@pytest.fixture
def sample_json_payload():
    """JSON данные для POST-запроса."""
    return {
        "id": 777,
        "is_new": True,
        "message": "Hello, is POST",
    }

@pytest.fixture
def sample_form_payload():
    """Данные для form-data POST-запроса."""
    return {
        "username": "tester_999",
        "password": "secret123",
        "remember": "true",
    }
@pytest.fixture
def list_query_data():
    """Словарь с параметрами, включающими список (для теста со списком)."""
    return {
        "page": 2,
        "tags": ["admin", "vip", "editor"]
    }