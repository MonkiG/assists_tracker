from typing import Dict
import uuid
from helpers.employee_code import generate_employee_code


def Employee(name: str, first_surname: str, last_surname: str) -> Dict[str, str]:
    first = name[:3]
    second = first_surname[:1]
    third = last_surname[:1]
    code = generate_employee_code(f"{first}{second}{third}".lower())

    return {
        "id": str(uuid.uuid4()),
        "code": f"{code}",
        "name": f"{name}",
        "firstSurname": f"{first_surname}",
        "lastSurname": f"{last_surname}",
    }
