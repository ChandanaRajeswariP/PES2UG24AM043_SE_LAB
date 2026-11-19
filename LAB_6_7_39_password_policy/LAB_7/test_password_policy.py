"""Hypothesis fuzz tests and regression examples for password-policy inputs."""

import math

import pytest
from hypothesis import given, settings, strategies as st

from password_policy import digit_ratio, first_character_type, split_credentials


arbitrary_input = st.one_of(
    st.text(),
    st.none(),
    st.integers(),
    st.floats(allow_nan=True, allow_infinity=True),
    st.binary(),
    st.lists(st.integers(), max_size=4),
)
structured_text = st.text(alphabet="abcXYZ019:!@._- \t", max_size=100)


@settings(max_examples=200, deadline=None)
@given(arbitrary_input)
def test_first_character_type_handles_arbitrary_inputs(value):
    result = first_character_type(value)
    if isinstance(value, str) and value:
        first = value[0]
        expected = "digit" if first.isdigit() else "letter" if first.isalpha() else "symbol"
        assert result == expected
    else:
        assert result is None


@settings(max_examples=200, deadline=None)
@given(structured_text)
def test_first_character_type_text_property(value):
    result = first_character_type(value)
    if not value:
        assert result is None
    else:
        assert result in {"digit", "letter", "symbol"}


@settings(max_examples=200, deadline=None)
@given(arbitrary_input)
def test_split_credentials_handles_arbitrary_inputs(value):
    result = split_credentials(value)
    if isinstance(value, str) and value.count(":") == 1:
        user, password = (part.strip() for part in value.split(":", maxsplit=1))
        expected = (user, password) if user and password else None
        assert result == expected
    else:
        assert result is None


@settings(max_examples=200, deadline=None)
@given(structured_text)
def test_split_credentials_text_property(value):
    result = split_credentials(value)
    if value.count(":") == 1:
        user, password = (part.strip() for part in value.split(":", maxsplit=1))
        assert result == ((user, password) if user and password else None)
    else:
        assert result is None


@settings(max_examples=200, deadline=None)
@given(arbitrary_input)
def test_digit_ratio_handles_arbitrary_inputs(value):
    result = digit_ratio(value)
    if isinstance(value, str) and value:
        expected = sum(character.isdigit() for character in value) / len(value)
        assert math.isclose(result, expected)
    else:
        assert result is None


@settings(max_examples=200, deadline=None)
@given(structured_text)
def test_digit_ratio_text_property(value):
    result = digit_ratio(value)
    if not value:
        assert result is None
    else:
        assert math.isfinite(result)
        assert 0 <= result <= 1


@pytest.mark.parametrize(
    "value, expected",
    [("7abc", "digit"), ("Alice", "letter"), ("!abc", "symbol")],
)
def test_first_character_examples(value, expected):
    assert first_character_type(value) == expected


@pytest.mark.parametrize(
    "value",
    [None, "", 7, b"abc", []],
)
def test_non_string_and_empty_inputs_are_rejected(value):
    assert first_character_type(value) is None
    assert split_credentials(value) is None
    assert digit_ratio(value) is None


@pytest.mark.parametrize("value", ["alice", "alice:", ":secret", "a:b:c", " : "])
def test_malformed_credentials_are_rejected(value):
    assert split_credentials(value) is None


def test_valid_examples():
    assert split_credentials(" alice : Secr3t ") == ("alice", "Secr3t")
    assert digit_ratio("Abc123") == pytest.approx(0.5)


def test_empty_password_is_rejected_by_character_helpers():
    assert first_character_type("") is None
    assert digit_ratio("") is None
