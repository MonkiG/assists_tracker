import cv2
import os
import numpy as np
from datetime import datetime


def init_model_training(data_path: str):
    labels, faceData = charge_training_images(data_path)
    training(faceData, labels)


def charge_training_images(data_path: str):
    employee_list = os.listdir(data_path)
    print("Lista de personas", employee_list)

    labels = []
    faceData = []
    label = 0

    for name_dir in employee_list:
        employee_path = f"{data_path}/{name_dir}"
        print("Leyendo imagenes")

        for file_name in os.listdir(employee_path):
            print(f"Rostros: {name_dir}/{file_name}")
            labels.append(label)

            faceData.append(cv2.imread(f"{employee_path}/{file_name}", 0))
            image = cv2.imread(f"{employee_path}/{file_name}", 0)

            # Muestra las imagenes con las que esta entrenando el modelo
            # cv2.imshow("image", image)
            # cv2.waitKey(10)

    label += 1
    cv2.destroyAllWindows()
    return labels, faceData


def training(faceData: list, labels: list):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    print("Entrenando...")
    face_recognizer.train(faceData, np.array(labels))

    # Guada el modelo
    nombre_modelo = f"FaceRecognizerModel-{datetime.now().strftime('%d-%m-%Y')}.xml"
    face_recognizer.write(os.path.join("..", "IAModels", nombre_modelo))
    print("Modelo guardado")
