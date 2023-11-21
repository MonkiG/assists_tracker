def get_hour(time: str):
    horas_str, minutor_str = time.split(":")
    return int(horas_str)
