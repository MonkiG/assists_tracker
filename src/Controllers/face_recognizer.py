import cv2
from helpers.get_model import get_model
import datetime
from Services.user_services import get_all_users
from Services.assists_services import (
    get_assist,
    add_assists_entry,
    add_assits_departure,
)
from helpers.get_hour import get_hour


def face_recognizer():
    employees_lists = get_all_users()

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

            date = datetime.datetime.now()
            date_now = date.date()
            date_time = date.time()
            current_hour = date_time.hour
            current_minutes = date_time.minute

            employee_code = employees_lists[result[0]]["code"]
            employee_assist = get_assist(employee_code, date_now)

            if result[1] < 100 and employee_assist == None:
                cv2.putText(
                    frame,
                    "{}".format(employees_lists[result[0]]["name"]),
                    (x, y - 35),
                    2,
                    1.1,
                    (0, 255, 0),
                    1,
                    cv2.LINE_AA,
                )

                cv2.putText(
                    frame,
                    f"{current_hour}:{current_minutes}",
                    (x, y - 5),
                    2,
                    1.1,
                    (0, 255, 0),
                    1,
                    cv2.LINE_AA,
                )

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                add_assists_entry(employee_code, f"{current_hour}:{current_minutes}")
            elif result[1] < 100 and (
                employee_assist != None
                and get_hour(employee_assist["entry"]) <= current_hour + 1
            ):
                cv2.putText(
                    frame,
                    "Entrada registrada",
                    (x, y - 20),
                    2,
                    0.8,
                    (0, 255, 0),
                    1,
                    cv2.LINE_AA,
                )
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            elif result[1] < 100 and (
                employee_assist != None
                and get_hour(employee_assist["entry"]) + 4 >= current_hour + 4
            ):
                cv2.putText(
                    frame,
                    "{}".format(employees_lists[result[0]]["name"]),
                    (x, y - 35),
                    2,
                    1.1,
                    (0, 255, 0),
                    1,
                    cv2.LINE_AA,
                )

                cv2.putText(
                    frame,
                    f"{current_hour}:{current_minutes}",
                    (x, y - 5),
                    2,
                    1.1,
                    (0, 255, 0),
                    1,
                    cv2.LINE_AA,
                )

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                add_assits_departure(employee_code, f"{current_hour}:{current_minutes}")
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
