import cv2
import os
import numpy as np
from datetime import datetime
from helpers.get_route import get_route
from Services.user_services import get_user


def init_model_training():
    labels, face_data = charge_training_images(get_route("Data"))
    training(face_data, labels)


def charge_training_images(data_path: str):
    exc = [".gitignore", "admin"]
    employee_list = [element for element in os.listdir(data_path) if element not in exc]
    employee_names_list = []
    for employee_code in employee_list:
        employee_name = get_user(employee_code)["name"]
        employee_names_list.append(employee_name)

    labels = []
    face_data = []
    label = 0

    for name_dir in employee_list:
        employee_images_path = f"{data_path}/{name_dir}/images"
        print("Leyendo imagenes")

        for file_name in os.listdir(employee_images_path):
            print(f"Rostros: {name_dir}/images/{file_name}")
            labels.append(label)

            face_data.append(cv2.imread(f"{employee_images_path}/{file_name}", 0))
            image = cv2.imread(f"{employee_images_path}/{file_name}", 0)

    label += 1
    cv2.destroyAllWindows()
    return labels, face_data


def training(faceData: list, labels: list):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    print("Entrenando...")
    face_recognizer.train(faceData, np.array(labels))

    # Guada el modelo
    nombre_modelo = f"FaceRecognizerModel-{datetime.now().strftime('%d-%m-%Y')}.xml"
    face_recognizer.write(os.path.join(get_route("IAModels"), nombre_modelo))
    print("Modelo guardado")
