import datetime
from unittest.mock import patch
import pytest
from src.files import JSONManager
from src.history import Record, OperationType

NOW = datetime.datetime(2024, 9, 25, 18, 31, 2)
DT_FORMAT = "%Y-%m-%d %H:%M:%S"


@pytest.fixture
def record():
    return Record(
        operation=OperationType.ENCRYPTING,
        input_text="abcd",
        output_text="abcd",
        shift=1,
        time=NOW
    )


@patch("src.files.json.dump")
def test_save_to_json(mock_save_to_json, record):
    filename = "history.json"
    expected_time = datetime.datetime.strftime(NOW, DT_FORMAT)
    expected_data = [{'input_text': 'abcd', 'operation': 'Encrypting',
                      'output_text': 'abcd', 'shift': 1, 'time': expected_time}]
    JSONManager.save_to_json([record], filename)
    actual_args = mock_save_to_json.call_args.args[0]
    assert actual_args == expected_data


@pytest.mark.parametrize("filename, expected", [
    ("history.json", [{"encrypted_text": "bcd", "shift": 1}]),
])
@patch("src.files.JSONManager.load_from_json")
def test_load_from_json(mock_load_from_json, filename, expected):
    mock_load_from_json.return_value = expected
    assert JSONManager.load_from_json(filename) == expected
    mock_load_from_json.assert_called_with(filename)
