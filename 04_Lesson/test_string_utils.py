import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# Тесты для метода capitalize

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("  ", "  "),
    ("123abc", "123abc"),
])


def test_capitalize_positive(input_str, expected,):
    assert string_utils.capitalize(input_str) == expected



@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("Pyton", "Pyton"),
    ("123456", "123456"),
    ("   ", "   ")
])


def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


def test_capitalize_none():
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


# Тесты для метода trim

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  Skypro", "Skypro"),
    ("    123", "123"),
])


def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("    ", ""),
])


def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


def test_trim_none():
    with pytest.raises(AttributeError):
        string_utils.trim(None)

# Тесты для метода contains

@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "S", True),
    ("Skypro", "o", True),
    ("Skypro", "x", False),
])


def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "a", False),
    ("Skypro", "g", False),
    ("Skypro", "e", False)])


def test_contains_(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected


def test_contains_none():
    with pytest.raises(AttributeError):
        string_utils.contains(None)



# Тесты для метода delete_symbol


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "p", "Skyro"),
    ("Skypro", "o", "Skypr")])


def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected



@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("Skypro", "z", "Skypro"),
    ("", "a", ""),
    ("   ", "S", "   ")])


def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


def test_delete_sumbol_none():
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None)
