import tkinter as tk
from typing import Dict


class Form:
    def __init__(self, root: tk.Tk, form_name: str) -> None:
        self.window = root
        self.window.title(f"Formulario {form_name}")
        self.entry_values = {}

    def start(self, values: list):
        for clave in values:
            label_clave = tk.Label(self.window, text=clave)
            if clave == "Contraseña":
                entry_clave = tk.Entry(self.window, show="*")
            else:
                entry_clave = tk.Entry(self.window)
            label_clave.pack()
            entry_clave.pack()
            self.entry_values[clave] = entry_clave

    def get_values(self):
        return {clave: entry.get() for clave, entry in self.entry_values.items()}

    def destroy_form(self):
        for label in self.window.winfo_children():
            if isinstance(label, tk.Label):
                label.destroy()

        for entry in self.window.winfo_children():
            if isinstance(entry, tk.Entry):
                entry.destroy()
        for btn in self.window.winfo_children():
            if isinstance(btn, tk.Button) and btn["text"] == "Submit":
                btn.destroy()
