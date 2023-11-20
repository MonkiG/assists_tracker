import cv2
from helpers.get_route import get_route
import os


def face_recognizer():
    exc = [".gitignore", "admin"]
    data_path = get_route("Data")
    list_filtered = [element for element in os.listdir(data_path) if element not in exc]

    print(list_filtered)
    # face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    # face_recognizer.read(get_route("IAModels/ModeloFaceFrontalData2023.xml"))

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        ret, frame = cap.read()
        if ret == False:
            print("No se pudo acceder a la web cam")
            break

        # Agregar el algoritmo de IA

        cv2.imshow("frame", frame)
        k = cv2.waitKey(1)
        if k == 27:
            break

        if (
            cv2.waitKey(1) == 27
            or cv2.getWindowProperty("frame", cv2.WND_PROP_VISIBLE) < 1
        ):
            break

    cap.release()
    cv2.destroyAllWindows()
