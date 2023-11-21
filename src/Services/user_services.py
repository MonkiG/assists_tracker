from Services.file_services import create_file, delete_folder, read_json
from helpers.get_route import get_route
from typing import Dict
import os

def create_user(userData: Dict[str, str], admin_password: str ):
    admin = _get_admin()
    if admin_password != admin["password"]:
        raise ValueError("Invalid credential!, admin password wrong")

    folder_path = get_route(f"Data/{userData['code']}")
    create_file(userData, folder_path , f"{userData["code"]}.json")

def delete_user(user_code: str, admin_password: str):
    admin = _get_admin()
    if admin_password != admin["password"]:
        raise ValueError("Invalid credential!, admin password wrong")

    folder_path = get_route(f"Data/{user_code}")
    delete_folder(folder_path)

def edit_user(user_code: str, new_user_data: Dict[str, str], admin_password: str):
    admin = _get_admin()
    if admin_password != admin["password"]:
        raise ValueError("Invalid credential!, admin password wrong")

    file_path = get_route(f"Data/{user_code}")
    user_saved = read_json(f"{file_path}\\{user_code}.json")
    user_updated = {
        **user_saved,
        **new_user_data
    }

    create_file(user_updated, f"{file_path}", f"{user_code}.json")
        
def get_user(user_code: str):
    file_path = get_route(f"Data/{user_code}")
    user_saved = read_json(f"{file_path}\\{user_code}.json")
    return user_saved

def get_all_users():
    exc = ["admin", "assists", ".gitignore"]
    file_path = get_route("Data")
    employees_folders = [element for element in os.listdir(file_path) if element not in exc]

    employees = []
    for employee_code in employees_folders:
        employee = get_user(employee_code)
        employees.append(employee)

    return employees
def _get_admin():
    file_path = get_route(f"Data/admin/admin.json")
    admin = read_json(file_path)
    return admin
