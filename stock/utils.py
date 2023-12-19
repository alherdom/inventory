import random
import string


def code_generator(code_length) -> str:
    string_code = string.digits + string.ascii_uppercase
    code = "".join(random.choice(string_code) for _ in range(code_length))
    return code
