def check_password(password):
    if len(password) < 8:
        return False
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    return has_digit and has_upper and has_lower


password = input("Enter a password: ")


if check_password(password):
    print("Password is valid.")
else:
    print("Password does not meet the criteria (at least 8 characters, one digit, one uppercase letter, and one lowercase letter).")
