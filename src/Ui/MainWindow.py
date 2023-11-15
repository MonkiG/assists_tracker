import tkinter as tk
from tkinter import Menu
import os


class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self._set_dimensions()
        self.window.title("Assists tracker")
        self.window.configure(bg="#ececec")
        self.window.iconbitmap(
            os.path.dirname(os.path.abspath(__file__)) + "\\assets\\icono.ico"
        )
        self._set_menubar(
            [
                {"label": "Add employee", "command": self.crear_usuario},
                {"label": "Delete employee", "command": self.delete_employee},
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
        # Establece valores en caso de que no sean pasados por parametro
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

    def crear_usuario(self):
        print("Nuevo")

    def delete_employee(self):
        print("delete employee")
