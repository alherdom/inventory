import random
import string


def code_generator() -> str:
    string_code = string.digits + string.ascii_uppercase
    return f"{random.choice(string_code)}{random.choice(string_code)}{random.choice(string_code)}"
