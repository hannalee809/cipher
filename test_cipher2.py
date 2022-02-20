import pytest
from cipher2 import *

@pytest.mark.parametrize("input_x, expected", 
       [pytest.param("A", "C", id = "uppercase_letter"), 
       pytest.param("!", "!", id = "not_letter"), 
       pytest.param("a", "c", id = "lowercase_letter"),
       pytest.param("z", "b", id = "returns_outside_lowercase_range"),
       pytest.param("Z", "B", id = "returns_outside_uppercase_range")
       ])

def test_shiftLetter(input_x, expected):
    assert shiftLetter(input_x, 2) == expected

@pytest.mark.parametrize("message_decrypted, message_encrypted",
        [pytest.param("abcdef", "hjlnpr", id = "all_lowercase"),
        pytest.param("aBcDef", "hJlNpr", id = "mixed_cases"), 
        pytest.param("ab c!e", "hj l!o", id = "spaces_and_symbols")])

def test_encipherShift(message_decrypted, message_encrypted):
    assert encipherShift(message_decrypted, "HIJKLM") == message_encrypted

@pytest.mark.parametrize("message_decrypted, message_encrypted",
        [pytest.param("abcdef", "hjlnpr", id = "all_lowercase"),
        pytest.param("aBcDef", "hJlNpr", id = "mixed_cases"), 
        pytest.param("ab c!e", "hj l!o", id = "spaces_and_symbols")])

def test_decipherShift(message_encrypted, message_decrypted):
    assert decipherShift(message_encrypted, "HIJKLM") == message_decrypted
