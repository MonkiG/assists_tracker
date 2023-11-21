import datetime
from Services.file_services import path_exists, create_folder, create_file, read_json
from helpers.get_route import get_route
from Models.Assit import Assist


def get_assist(employee_code: str, date: datetime.datetime.date):
    file_path = get_route(f"Data/assists/{date}")
    assist_saved = read_json(f"{file_path}\\{employee_code}.json")
    return assist_saved


def add_assists_entry(employee_code: str, entry_time: str):
    current_date = datetime.datetime.now().date()
    folder_path = get_route(f"Data/assists/{current_date}")
    if not path_exists(folder_path):
        create_folder(folder_path)
    assist_model = Assist({"entry": entry_time}, employee_code)
    create_file(assist_model, folder_path, f"{employee_code}.json")


def add_assits_departure(employee_code: str, departure_time: str | int = ""):
    current_date = datetime.datetime.now().date()
    file_path = get_route(f"Data/assists/{current_date}")
    assist_saved = get_assist(employee_code, current_date)
    assist_updated = {**assist_saved, "departure": str(departure_time)}

    create_file(assist_updated, f"{file_path}", f"{employee_code}.json")
