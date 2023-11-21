from typing import Dict
import uuid


def Assist(
    time: Dict[str, str],
    employee_code: str,
):
    print(time)
    return {"id": str(uuid.uuid4()), "code": employee_code, **time}
