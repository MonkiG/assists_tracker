import tkinter as tk


def get_screen_size() -> tuple:
    """
    Obtiene las dimensiones de la pantalla.

    Returns:
        tuple: Una tupla con las dimensiones (ancho, altura) de la pantalla.
    """
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return (screen_width, screen_height)
