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
            columna1, text="Verificar", bg="#0693e3", fg="#fff", width=15, command=self.verificar
        )
        boton_verificar.pack(pady=10)

        frame_derecha = tk.Frame(frame, bg="#EFEAE9")
        frame_derecha.pack(side="left")

        canvas = tk.Canvas(frame_derecha, width=750, height=750, bg="#EFEAE9")
        canvas.pack()
        canvas.create_rectangle(5, 5, 750, 750, outline="#202123", width=5)

        self._set_menubar(
            [
                {"label": "Add employee", "command": self.crear_usuario},
                {"label": "Delete employee", "command": self.eliminar_usuario},
            ]
        )

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
        screen_width = screen_width if screen_width is not None else self.window.winfo_screenwidth()
        screen_height = screen_height if screen_height is not None else self.window.winfo_screenheight()
        self.window.geometry(f"{screen_width}x{screen_height}+{x}+{y}")

    def start_window(self):
        self.window.mainloop()

    def crear_usuario(self):
        crear_usuario = Toplevel(self.window, bg="#EFEAE9")
        crear_usuario.geometry("400x300" )
        crear_usuario.title("Crear usuario")

        # Etiqueta y entrada para el nombre
        lbl_nombre = tk.Label(crear_usuario, text="Ingresa tu nombre:")
        lbl_nombre.pack(pady=10)
        entry_nombre = tk.Entry(crear_usuario, width=30)
        entry_nombre.pack(pady=5)

        # Etiqueta y entrada para el apeido paterno
        lbl_nombre = tk.Label(crear_usuario, text="Ingresa tu apeido paterno:")
        lbl_nombre.pack(pady=10)
        entry_apeido1 = tk.Entry(crear_usuario, width=30)
        entry_apeido1.pack(pady=5)

        # Etiqueta y entrada para el apeido paterno
        lbl_nombre = tk.Label(crear_usuario, text="Ingresa tu apeido materno:")
        lbl_nombre.pack(pady=10)
        entry_apeido2 = tk.Entry(crear_usuario, width=30)
        entry_apeido2.pack(pady=5)


        # Lambda se utiliza para pasar los valores de entry_nombre y entry_contrasena
        btn_aceptar = tk.Button(crear_usuario, text="Aceptar", command=lambda: self.guardar_usuario(entry_nombre.get(), entry_contrasena.get()))
        btn_aceptar.pack(pady=20)    

    def eliminar_usuario(self):
        # Obtener el nombre del usuario a eliminar
        nombre_usuario = self.entry_nombre.get()

        # Aquí puedes agregar la lógica para eliminar el usuario con el nombre proporcionado
        print(f"Usuario eliminado: {nombre_usuario}")

    def verificar(self):
        # Agrega la lógica para verificar aquí
        pass

    def guardar_usuario(self, nombre, contrasena):
        # Guardar la información del usuario en un archivo txt
        with open('usuarios.json', 'a') as archivo:
            archivo.write(f"{nombre},{contrasena}\n")
        print("Usuario guardado exitosamente.")

# Crear una instancia de la clase MainWindow y mostrar la ventana
app = MainWindow()
app.start_window()
