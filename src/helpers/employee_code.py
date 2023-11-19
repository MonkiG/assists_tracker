import secrets


def generate_employee_code(first_section: str, code_len: str = 4) -> str:
    employee_code = first_section + str(secrets.token_hex(int(code_len / 2)))
    return employee_code
