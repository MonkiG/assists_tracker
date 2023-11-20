import cv2
from helpers.get_route import get_route
from helpers.get_model import get_model
import os
import datetime
from Services.user_services import get_user


def face_recognizer():
    exc = [".gitignore", "admin"]
    data_path = get_route("Data")
    list_filtered = [element for element in os.listdir(data_path) if element not in exc]

    employee_names_list = []
    for employee_code in list_filtered:
        employee_name = get_user(employee_code)["name"]
        employee_names_list.append(employee_name)

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    model = get_model()
    face_recognizer.read(model)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    face_classif = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    while True:
        ret, frame = cap.read()
        if ret == False:
            print("No se pudo acceder a la web cam")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = face_classif.detectMultiScale(gray, 1.3, 5)
        for x, y, w, h in faces:
            rostro = auxFrame[y : y + h, x : x + w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(rostro)

            if result[1] < 100:
                cv2.putText(
                    frame,
                    "{}".format(employee_names_list[result[0]]),
                    (x, y - 35),
                    2,
                    1.1,
                    (0, 255, 0),
                    1,
                    cv2.LINE_AA,
                )
                date_time = datetime.datetime.now().time()
                hour = date_time.hour
                minutes = date_time.minute
                cv2.putText(
                    frame,
                    f"{hour}:{minutes}",
                    (x, y - 5),
                    2,
                    1.1,
                    (0, 255, 0),
                    1,
                    cv2.LINE_AA,
                )

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else:
                cv2.putText(
                    frame,
                    "Desconocido",
                    (x, y - 20),
                    2,
                    0.8,
                    (0, 0, 255),
                    1,
                    cv2.LINE_AA,
                )
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

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
