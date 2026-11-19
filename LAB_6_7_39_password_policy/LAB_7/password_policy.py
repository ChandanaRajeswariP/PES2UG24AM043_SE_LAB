"""Defensive helpers for validating password-related input."""


def first_character_type(password):
    """Classify the first character, or return None for invalid input."""
    if not isinstance(password, str) or not password:
        return None

    first = password[0]
    if first.isdigit():
        return "digit"
    if first.isalpha():
        return "letter"
    return "symbol"


def split_credentials(text):
    """Split one non-empty username:password pair; reject malformed input."""
    if not isinstance(text, str) or text.count(":") != 1:
        return None

    user, password = (part.strip() for part in text.split(":", maxsplit=1))
    if not user or not password:
        return None
    return user, password


def digit_ratio(password):
    """Return the fraction of digit characters, or None for invalid input."""
    if not isinstance(password, str) or not password:
        return None
    return sum(character.isdigit() for character in password) / len(password)


def _display_result(label, result):
    """Print a result or a friendly validation message."""
    if result is None:
        print(f"{label}: Invalid input")
    else:
        print(f"{label}: {result}")


def main():
    """Run the interactive demonstration without crashing on bad input."""
    print("==== Running first_character_type ====")
    user_input = input("Enter a password: ")
    _display_result("First Character Type", first_character_type(user_input))

    print("\n==== Running split_credentials ====")
    user_input = input("Enter user:password (e.g. alice:Secret1): ")
    _display_result("User and Password", split_credentials(user_input))

    print("\n==== Running digit_ratio ====")
    user_input = input("Enter a password to measure: ")
    _display_result("Digit Ratio", digit_ratio(user_input))


if __name__ == "__main__":
    main()
