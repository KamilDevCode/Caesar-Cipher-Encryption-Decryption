import pytest
from src.ciphers.caeser import CeaserCipher


@pytest.fixture
def ceaser_cipher():
    yield CeaserCipher()


@pytest.mark.parametrize("text, shift", [
    ("xyz", -1),
    ("abc", -2),
])
def test_for_encrypt_with_negative_shift_should_raise_error(ceaser_cipher, text, shift):
    with pytest.raises(ValueError, match="Shift value cannot be negative."):
        ceaser_cipher.encrypt(text, shift)


@pytest.mark.parametrize("text, shift", [
    ("hello", -1),
    ("abc", -2),
])
def test_for_decrypt_with_negative_shift_should_raise_error(ceaser_cipher, text, shift):
    with pytest.raises(ValueError, match="Shift value cannot be negative."):
        ceaser_cipher.decrypt(text, shift)


@pytest.mark.parametrize("text, shift, expected", [
    ("hello", 0, "hello"),
    ("Caesar", 0, "Caesar"),
])
def test_zero_shift_should_return_original_text(ceaser_cipher, text, shift, expected):
    assert ceaser_cipher.encrypt(text, shift) == expected
    assert ceaser_cipher.decrypt(text, shift) == expected


@pytest.mark.parametrize("text, shift, expected", [
    ("abc", 1, "bcd"),
    ("abc", 2, "cde"),
    ("abc", 3, "def"),
    ("abc", 4, "efg"),
    ("abc", 5, "fgh"),
])
def test_encrypt_should_return_shifted_text_correctly(ceaser_cipher, text, shift, expected):
    assert ceaser_cipher.encrypt(text, shift) == expected


@pytest.mark.parametrize("text, shift, expected", [
    ("abc", 1, "bcd"),
    ("abc", 2, "cde"),
    ("abc", 3, "def"),
    ("abc", 4, "efg"),
    ("abc", 5, "fgh"),
])
def test_decrypt_should_return_shifted_text_correctly(ceaser_cipher, text, shift, expected):
    assert ceaser_cipher.decrypt(text, shift) == expected


@pytest.mark.parametrize("text, shift, expected", [
    ("ąźć", 1, "ćżę"),
])
def test_encrypt_polish_vowels_alphabet_should_return_shifted_text_correctly(ceaser_cipher, text, shift, expected):
    assert ceaser_cipher.encrypt(text, shift) == expected


@pytest.mark.parametrize("text, shift, expected", [
    ("ąźć", 1, "ćżę"),
    ("ćżę", 1, "ęał"),

])
def test_decrypt_polish_vowels_alphabet_should_return_shifted_text_correctly(ceaser_cipher, text, shift, expected):
    assert ceaser_cipher.decrypt(text, shift) == expected


@pytest.mark.parametrize("text, shift, expected", [
    ("ABC", 1, "BCD"),
    ("ABC", 2, "CDE"),
    ("ABC", 3, "DEF"),
    ("ABC", 4, "EFG"),
    ("ABC", 5, "FGH"),
])
def test_encrypt_uppercase_polish_alphabet(ceaser_cipher, text, shift, expected):
    assert ceaser_cipher.encrypt(text, shift) == expected


@pytest.mark.parametrize("text, shift, expected", [
    ("ABC", 1, "BCD"),
    ("ABC", 2, "CDE"),
    ("ABC", 3, "DEF"),
    ("ABC", 4, "EFG"),
    ("ABC", 5, "FGH"),
])
def test_decrypt_uppercase_polish_alphabet(ceaser_cipher, text, shift, expected):
    assert ceaser_cipher.decrypt(text, shift) == expected
