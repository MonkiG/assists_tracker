import pandas as pd
from Services.assists_services import get_assist
from helpers.get_route import get_route
import os
import datetime


def export_current_assists(excel_path: str):
    """
    Exporta las asistencias de hoy a excel
    """
    current_date = datetime.datetime.now().date()
    current_date_assists_path = get_route(f"Data/assists/{current_date}")
    employees_assists_files = os.listdir(current_date_assists_path)
    employees_assists_data = []

    for data in employees_assists_files:
        employee_code = data.split(".json")[0]
        assist = get_assist(employee_code, current_date)
        employees_assists_data.append(assist)

    data_frame = pd.DataFrame(employees_assists_data)
    data_frame.to_excel(excel_path, index=False)
