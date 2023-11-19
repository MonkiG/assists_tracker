import os
import json
import shutil


def create_file(data, folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)

    if not path_exists(folder_path):
        create_folder(folder_path)

    print("file name", file_name)
    with open(file_path, "w") as file:
        print("Creando archivo")
        if ".json" in file_name:
            file.write(json.dumps(data, indent=2))
        else:
            file.write(str(data))
        print("Archivo creado")

    return file_path


def delete_file(file_path: str):
    try:
        print(f"Eliminando archivo: {file_path}")
        os.remove(file_path)
        print("Archivo eliminado correctamente")
    except FileNotFoundError:
        print(f"El archivo {file_path} no existe.")
    except Exception as e:
        print(f"Error al intentar eliminar el archivo {file_path}: {e}")


def create_folder(
    folder_path: str,
    folder_name: str = "",
):
    new_folder_path = os.path.join(folder_path, folder_name)
    print("Creando carpeta")
    os.makedirs(new_folder_path)
    print(f"Carpeta creada: {new_folder_path}")

    return new_folder_path


def delete_folder(folder_path: str):
    try:
        print(f"Eliminando folder {folder_path}")
        shutil.rmtree(folder_path)
        print("Folder eliminado correctamente")
    except FileNotFoundError:
        print(f"La carpeta {folder_path} no existe.")
    except OSError as e:
        print(f"Error al intentar eliminar la carpeta {folder_path}: {e}")


def path_exists(path: str) -> bool:
    """
    Verify if a path exists
    """

    return os.path.exists(path)


def read_json(file_path: str):
    """
    Lee la informacion del archivo json pasado por parametro,
    retorna dicha informacion en forma de diccionario
    """
    with open(file_path, "r") as file:
        json_data = json.load(file)

    return json_data
