from Services.file_services import create_file, delete_folder, read_json
from typing import Dict

def create_user(userData: Dict[str, str], folder_path: str ):
    create_file(userData, folder_path , f"{userData["code"]}.json")

def delete_user(user_code: str):
    folder_path = f"C:\\Users\\mon_e\\OneDrive\\Escritorio\\Proyectos\\UNIVERSIDAD\\assists_tracker\\Data\\{user_code}"
    delete_folder(folder_path)

def edit_user(user_code: str, new_user_data: Dict[str, str]):
    file_path = f"C:\\Users\\mon_e\\OneDrive\\Escritorio\\Proyectos\\UNIVERSIDAD\\assists_tracker\\Data\\{user_code}"
    user_saved = read_json(f"{file_path}\\{user_code}.json")
    user_updated = {
        **user_saved,
        **new_user_data
    }

    create_file(user_updated, f"{file_path}", f"{user_code}.json")
        
def get_user(user_code: str):
    file_path = f"C:\\Users\\mon_e\\OneDrive\\Escritorio\\Proyectos\\UNIVERSIDAD\\assists_tracker\\Data\\{user_code}"
    user_saved = read_json(f"{file_path}\\{user_code}.json")
    return user_saved
