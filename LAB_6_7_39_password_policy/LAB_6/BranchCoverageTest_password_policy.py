"""Lab 6 tests that exercise both outcomes of each password-policy decision."""

from password_policy import check_password, strength, suggest_fix


def test_length_validation_branches():
    assert "too short" in check_password("abc")
    assert "too long" in check_password("a" * 65)
    assert "too short" not in check_password("Abcdef1!")
    assert "too long" not in check_password("Abcdef1!")


def test_common_password_branch():
    assert "common" in check_password("password")
    assert "common" not in check_password("Abcdef1!")


def test_character_class_branches():
    assert check_password("Abcdef1!") == []
    assert "no uppercase" in check_password("abcdef1!")
    assert "no lowercase" in check_password("ABCDEF1!")
    assert "no digit" in check_password("Abcdefgh!")
    assert "no special" in check_password("Abcdefg1")


def test_strength_branches():
    assert strength("Abcdef1!") == "good"
    assert strength("Abcdefgh123!XY") == "strong"
    assert strength("abcdefg1") == "weak"
    assert strength("") == "very weak"


def test_suggest_fix_branches():
    assert suggest_fix([]) == "none needed"
    assert suggest_fix(["too short"]) == "add more characters"
    assert suggest_fix(["common"]) == "avoid common passwords"
    assert suggest_fix(["no uppercase"]) == "add uppercase"
    assert suggest_fix(["too long"]) == "shorten it"
