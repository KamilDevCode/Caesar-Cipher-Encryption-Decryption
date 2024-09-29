from unittest.mock import patch
import pytest
from src.history import Record, OperationType
from datetime import datetime
from src.facade import Menu


@pytest.fixture
def example_record():
    yield Record(
        operation=OperationType.ENCRYPTING,
        input_text='abc',
        output_text='bcd',
        shift=1,
        time=datetime.now()
    )


def test_record_to_dict(example_record):
    record_dict = example_record.to_dict()
    assert record_dict['operation'] == "Encrypting"
    assert record_dict['input_text'] == "abc"
    assert record_dict['output_text'] == "bcd"
    assert isinstance(record_dict['time'], str)


@patch('src.files.JSONManager.load_from_json')
def test_record_str(mock_load_from_json, example_record):
    mock_load_from_json.return_value = [{"encrypted_text": "bcd", "shift": 1}]
    record_str = str(example_record)

    assert "Encrypting" in record_str
    assert "abc" in record_str
    assert "bcd" in record_str
    assert datetime.now().strftime("%Y") in record_str


@pytest.fixture()
def example_record_decrypt():
    yield Record(
        operation=OperationType.DECRYPTING,
        input_text='abc',
        output_text='bcd',
        shift=1,
        time=datetime.now()
    )


def test_record_to_dict_decrypt(example_record_decrypt):
    record_dict = example_record_decrypt.to_dict()
    assert record_dict['operation'] == "Decrypting"
    assert record_dict['input_text'] == "abc"
    assert record_dict['output_text'] == "bcd"
    assert isinstance(record_dict['time'], str)


@patch('src.files.JSONManager.load_from_json')
def test_record_str_decrypt(mock_load_from_json, example_record_decrypt):
    mock_load_from_json.return_value = [{"decrypted_text": "bcd", "shift": 1}]

    record_str = str(example_record_decrypt)

    assert "Decrypting" in record_str
    assert "abc" in record_str
    assert "bcd" in record_str
    assert datetime.now().strftime("%Y") in record_str


@pytest.fixture()
def menu():
    yield Menu()


@patch('src.facade.Menu.display_operations', return_value=(
        "Operations:\n1. Encrypt\n2. Decrypt\n3. Save History to JSON file\n4. "
        "Load History from JSON file\n5. Display Operations\n6. Exit"))
def test_display_menu(mock_display_operations, menu):

    expected_output = ("Operations:\n1. Encrypt\n2. Decrypt\n3."
                       " Save History to JSON file\n4."
                       " Load History from JSON file\n5. "
                       "Display Operations\n6. Exit")

    assert menu.display_operations() == expected_output
