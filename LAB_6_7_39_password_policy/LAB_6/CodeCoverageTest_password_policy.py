"""Lab 6 test suite focused on executing every password-policy statement."""

from password_policy import check_password, strength, suggest_fix


def test_check_password_detects_short_password_and_missing_categories():
    assert check_password("ab") == [
        "too short",
        "no uppercase",
        "no digit",
        "no special",
    ]


def test_check_password_detects_long_common_and_missing_categories():
    issues = check_password("a" * 65)
    assert "too long" in issues
    assert "no uppercase" in issues
    assert "no digit" in issues
    assert "no special" in issues


def test_check_password_detects_common_password():
    assert "common" in check_password("password")


def test_check_password_accepts_mixed_character_classes():
    assert check_password("Abcdef1!") == []


def test_strength_good_strong_weak_and_very_weak():
    assert strength("Abcdef1!") == "good"
    assert strength("Abcdefgh123!XY") == "strong"
    assert strength("abcdefg1") == "weak"
    assert strength("") == "very weak"


def test_suggest_fix_for_each_response_path():
    assert suggest_fix([]) == "none needed"
    assert suggest_fix(["too short"]) == "add more characters"
    assert suggest_fix(["common"]) == "avoid common passwords"
    assert suggest_fix(["no uppercase"]) == "add uppercase"
    assert suggest_fix(["too long"]) == "shorten it"
