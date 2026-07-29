import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("    ", ""),
    ("  pyton","pyton"),
    ("123abc", "123Abc")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("pyton", "pyton"),
    ("05 мая 2026   ", "05 мая 2026"),
    ("",""),
    ("12456","123456"),
    ("   abc","abc")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("str1, str2, result",
     [("Skypro", "o", True),
      ("Skypro", "k", True),
      ("Skypro", "pro", True),])
def test_strib_positive(str1, str2, result):
    string_utils=StringUtils()
    res=stringUtils.contains(str1, str2)
    assert res == result


@pytest.mark.negative
@pytest.mark.parametrize("str1, str2, result", [
    ("Skypro", "a", false),
    ("Skypro", "g", false),
    ("Skypro", "e", felse)])
def test_strib_negative(str1, str2, result):
    string_utils = StringUtils








