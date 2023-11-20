import os
from pathlib import Path


def get_route(routes: str = "src"):
    # Obtener la ruta del proyecto
    proyect_dir = proyect_route()

    # Construir la ruta completa
    file_path = os.path.join(proyect_dir, routes)
    return file_path


def proyect_route(route: str = None):
    return Path(__file__).parent.parent.parent
