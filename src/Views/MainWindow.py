import tkinter as tk
from tkinter import messagebox
from helpers.get_route import get_route
from Controllers.register_employee import init_register
from Controllers.face_recognizer import face_recognizer
from Services.user_services import create_user, delete_user, get_user, edit_user
from Models.User import Employee
from Views.Foms import Form
import time

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self._set_dimensions(450, 450)
        self.window.title("Assists tracker")
        self.window.configure(bg="#ececec")
        self.window.iconbitmap(get_route("src/Views/assets/icono.ico"))
        self.buttons_data = [
            {
                "name": "startBtn",
                "text": "Empezar reconocimiento",
                "command": face_recognizer,
            },
            {
                "name": "addEmployeeBtn",
                "text": "Añadir nuevo empleado",
                "command": self._handle_add_employee,
            },
            {
                "name": "deleteEmployeeBtn",
                "text": "Eliminar empleado",
                "command": self._handle_delete_employee,
            },
            {
                "name": "editEmployeeBtn",
                "text": "Editar empleado",
                "command": lambda: print("Editar empleado"),
            },
            {
                "name": "getEmployeeBtn",
                "text": "Obtener empleado",
                "command": self._handle_get_employee,
            },
        ]
        self.buttons_ui = []
        self._set_buttons()

    def _set_dimensions(
        self,
        screen_width: int = None,
        screen_height: int = None,
    ):
        screen_width = (
            screen_width
            if screen_width is not None
            else self.window.winfo_screenwidth()
        )
        screen_height = (
            screen_height
            if screen_height is not None
            else self.window.winfo_screenheight()
        )

        self._center(self.window, screen_width, screen_height)

    def _center(self, win, width, height):
        """
        centers a tkinter window
        :param win: the main window or Toplevel window to center
        """
        win.update_idletasks()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry("{}x{}+{}+{}".format(width, height, x, y))
        win.deiconify()

    def _set_buttons(self):
        for btn in self.buttons_data:
            buttonUi = tk.Button(self.window, text=btn["text"], command=btn["command"])
            buttonUi.pack()
            self.buttons_ui.append(buttonUi)

    def _handle_delete_employee(self):
        self.restart()
        form = Form(self.window, "Delete employee")
        form.start(["Codigo de empleado", "Contraseña"])

        def handle_button():
            values = form.get_values()
            delete_user(values["Codigo de empleado"], values["Contraseña"])
            messagebox.showinfo("Empleado eliminado", "Empleado eliminado correctamente")
            form.destroy_form()

        button_submit = tk.Button(self.window, text="Submit", command=lambda: handle_button())
        button_submit.pack()

    def _handle_add_employee(self):
        self.restart()
        form = Form(self.window, "Add employee")
        form.start(["Nombre", "Apellido paterno", "Apellido materno", "Contraseña"])

        def handle_button():
            values = form.get_values()
            print("values: ", values)
            new_employee = Employee(
                values["Nombre"], values["Apellido paterno"], values["Apellido materno"]
            )
            create_user(new_employee, values["Contraseña"])
            messagebox.showinfo("Reconocimiento de entrenamiento", "Empezando el reconocimiento inicial en 10 segundos \n posicionece en un espacio bien iluminado")
            time.sleep(10)
            init_register(new_employee["code"])
            messagebox.showinfo("Empleado registrado", f"Empleado registrado correctamente \n Codigo del empleado: {new_employee["code"]}")
            form.destroy_form()

        button_submit = tk.Button(
            self.window, text="Submit", command=lambda: handle_button()
        )
        button_submit.pack()

    # def _handle_edit_employee(self):
    #     self.restart()
    #     form = Form(self.window, "Add employee")
    #     form.start(["Codigo empleado","Nombre", "Apellido paterno", "Apellido materno", "Contraseña"])

    #     def handle_button():
    #         values = form.get_values()
    #         edit_user(values["Codigo empleado"],)


    def _handle_get_employee(self):
        self.restart()
        form = Form(self.window, "Get employee")
        form.start(["Codigo empleado"])
        def handle_button():
            values = form.get_values()
            employee = get_user(values["Codigo empleado"])
            text_widget = tk.Text(self.window)
            text_widget.pack()

            for key, value in employee.items():
                text_widget.insert(tk.END, f"{key}: {value} \n")
                
            
            form.destroy_form()

        button_submit = tk.Button(
            self.window, text="Submit", command=lambda: handle_button()
        )
        button_submit.pack()

    def start_window(self):
        self.window.mainloop()

    def restart(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self._set_buttons()
# frame_izquierda = tk.Frame(frame, bg="#EFEAE9")
# frame_izquierda.pack(side="left", padx=10)

# titulo = tk.Label(
#     frame_izquierda,
#     text="Introduce el nombre del usuario:",
#     font=("Arial", 14, "bold"),
#     bg="#EFEAE9",
#     fg="#000",
# )
# titulo.pack(pady=10, anchor="center")

# self.entry_nombre = tk.Entry(frame_izquierda, width=27)
# self.entry_nombre.pack(pady=10, anchor="center")

# frame_columnas = tk.Frame(frame_izquierda, bg="#EFEAE9")
# frame_columnas.pack()

# columna1 = tk.Frame(frame_columnas, bg="#EFEAE9")
# columna1.pack(side="left", padx=10)

# boton_verificar = tk.Button(
#     columna1,
#     text="Verificar",
#     bg="#0693e3",
#     fg="#fff",
#     width=15,
#     command=self.verificar,
# )
# boton_verificar.pack(pady=10)

# self.canvas.create_rectangle(
#     5, 5, 750, 750, outline="#202123", width=5, tag="camara"
# )
