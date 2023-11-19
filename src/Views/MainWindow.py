import cv2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Menu, Toplevel


class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self._set_dimensions()
        self.window.title("Assists tracker")
        self.window.configure(bg="#ececec")

        frame = tk.Frame(self.window, bg="#EFEAE9")
        frame.pack(pady=20)

        frame_izquierda = tk.Frame(frame, bg="#EFEAE9")
        frame_izquierda.pack(side="left", padx=10)

        titulo = tk.Label(
            frame_izquierda,
            text="Introduce el nombre del usuario:",
            font=("Arial", 14, "bold"),
            bg="#EFEAE9",
            fg="#000",
        )
        titulo.pack(pady=10, anchor="center")

        self.entry_nombre = tk.Entry(frame_izquierda, width=27)
        self.entry_nombre.pack(pady=10, anchor="center")

        frame_columnas = tk.Frame(frame_izquierda, bg="#EFEAE9")
        frame_columnas.pack()

        columna1 = tk.Frame(frame_columnas, bg="#EFEAE9")
        columna1.pack(side="left", padx=10)

        boton_verificar = tk.Button(
            columna1,
            text="Verificar",
            bg="#0693e3",
            fg="#fff",
            width=15,
            command=self.verificar,
        )
        boton_verificar.pack(pady=10)

        frame_derecha = tk.Frame(frame, bg="#EFEAE9")
        frame_derecha.pack(side="left")

        self.canvas = tk.Canvas(frame_derecha, width=750, height=750, bg="#EFEAE9")
        self.canvas.pack()
        self.canvas.create_rectangle(
            5, 5, 750, 750, outline="#202123", width=5, tag="camara"
        )

        self._set_menubar(
            [
                {"label": "Add employee", "command": self.crear_usuario},
                {"label": "Delete employee", "command": self.eliminar_usuario},
            ]
        )

        # Inicialización de la cámara y llamada a la función para actualizar el rectángulo
        self.cap = cv2.VideoCapture(0)
        self.photo = None  # Agregamos esta línea
        self.update_camera()

    def _set_menubar(self, commands: list):
        menubar = Menu(self.window)

        for comm in commands:
            menubar.add_command(label=comm["label"], command=comm["command"])

        self.window.config(menu=menubar)

    def _set_dimensions(
        self,
        screen_width: int = None,
        screen_height: int = None,
        x: int = 0,
        y: int = 0,
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
        self.window.geometry(f"{screen_width}x{screen_height}+{x}+{y}")

    def start_window(self):
        self.window.mainloop()

    def update_camera(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            self.photo = ImageTk.PhotoImage(image=img)

            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW, tag="camara")
            self.window.after(10, self.update_camera)
        else:
            self.window.after(10, self.update_camera)

    def verificar(self):
        print("verificar")

    def crear_usuario(self):
        crear_usuario = Toplevel(self.window, bg="#EFEAE9")
        crear_usuario.geometry("400x300")
        crear_usuario.title("Crear")

    def eliminar_usuario(self):
        print("Eliminar usuario")
