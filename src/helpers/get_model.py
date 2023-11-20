import os
from helpers.get_route import get_route


def get_model():
    files = os.listdir(get_route("IAModels"))
    model_files = [file for file in files if file.endswith(".xml")]
    model_files.sort(
        key=lambda x: os.path.getatime(os.path.join(get_route("IAModels"), x)),
        reverse=True,
    )

    return os.path.join(get_route("IAModels"), model_files[0])
