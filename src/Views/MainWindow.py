import tkinter as tk
from helpers.get_route import get_route


class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self._set_dimensions(450, 450)
        self.window.title("Assists tracker")
        self.window.configure(bg="#ececec")
        self.window.iconbitmap(get_route("src/Views/assets/icono.ico"))
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
        buttons = [
            {
                "name": "startBtn",
                "text": "Empezar reconocimiento",
                "command": lambda: print("Empezar reconocimiento"),
            },
            {
                "name": "addEmployeeBtn",
                "text": "Añadir nuevo empleado",
                "command": lambda: print("Añadir empleado"),
            },
            {
                "name": "deleteEmployeeBtn",
                "text": "Eliminar empleado",
                "command": lambda: print("Eliminar empleado"),
            },
            {
                "name": "editEmployeeBtn",
                "text": "Editar empleado",
                "command": lambda: print("Editar empleado"),
            },
            {
                "name": "getEmployeeBtn",
                "text": "Obtener empleado",
                "command": lambda: print("Obtener empleado"),
            },
        ]

        for btn in buttons:
            buttonUi = tk.Button(self.window, text=btn["text"], command=btn["command"])
            buttonUi.pack()

    def start_window(self):
        self.window.mainloop()


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
