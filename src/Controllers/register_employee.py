import cv2
from typing import Dict
from helpers.get_route import get_route
from helpers.get_screen_size import get_screen_size
from Services.file_services import create_folder


def init_register(employee_code):
    try:
        folder = create_folder(get_route(f"Data/{employee_code}"), "images")
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        videoLoop(folder, cap)
    except ValueError as e:
        print("Contraseña equivocada: ", e)


def videoLoop(employee_path: str, cap: cv2.VideoCapture):
    face_classif = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    counter_employee_pictures: int = 0
    (screen_width, screen_height) = get_screen_size()

    while True:
        ret, frame = cap.read()
        if ret == False:
            print("No se pudo activar la camara")
            break

        # frame = imutils.resize(frame, width=screen_width, height=screen_height)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        aux_frame = frame.copy()

        faces = face_classif.detectMultiScale(gray, 1.3, 5)

        # Bucle que muestra un rectangulo y ubica la cara
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            rostro = aux_frame[y : y + h, x : x + w]
            rostro = cv2.resize(rostro, (720, 720), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(
                f"{employee_path}/rostro_{counter_employee_pictures}.jpg", rostro
            )
            counter_employee_pictures = counter_employee_pictures + 1

        cv2.imshow("frame", frame)  # Muestra las imagenes guardadas (Creo xd)
        # cv2.setWindowProperty("frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # Escucha la tecla del teclado
        key = cv2.waitKey(1)

        # Rompe el bucle de la camara
        if key == 27 or counter_employee_pictures >= 300:
            break

        if (
            cv2.waitKey(1) == 27
            or cv2.getWindowProperty("frame", cv2.WND_PROP_VISIBLE) < 1
        ):
            break

    cap.release()
    cv2.destroyAllWindows()
