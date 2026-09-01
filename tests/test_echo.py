
from src.echo import get_echo_data


def test_get_none_param():
    data = get_echo_data()
    assert "headers" in data

