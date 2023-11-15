import cv2
import os
import imutils


def init_register(employee_name="Ramon"):
    data_path = "C:\\Users\\mon_e\\OneDrive\\Escritorio\\Proyectos\\UNIVERSIDAD\\AsitenciasTracker\\Data"

    employee_path = create_employee_folder(
        employee_name, data_path
    )  # Quitar valor hardcodeado
    cap, face_classif = set_capture_video()
    videoLoop(cap, face_classif, employee_path)

    cap.release()
    cv2.destroyAllWindows()


def create_employee_folder(employee_name: str, data_path: str):
    employee_path = f"{data_path}/{employee_name}"

    if not os.path.exists(employee_path):
        print("Creando carpeta de empleado")
        os.makedirs(employee_path)
        print(f"Carpeta creata: {employee_path}")

    return employee_path


def set_capture_video():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    face_classif = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    return (cap, face_classif)


def videoLoop(
    cap: cv2.VideoCapture, face_classif: cv2.CascadeClassifier, employee_path: str
):
    counter_employee_pictures: int = 0

    while True:
        ret, frame = cap.read()
        if ret == False:
            print("No se pudo activar la camara")
            break

        frame = imutils.resize(frame, width=320)
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

        # Escucha la tecla del teclado
        key = cv2.waitKey(1)

        # Rompe el bucle de la camara
        if key == 27 or counter_employee_pictures >= 300:
            break

        if cv2.waitKey(1) == 27:
            break
