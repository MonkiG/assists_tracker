from Views.MainWindow import MainWindow
from Services.export_services import export_current_assists

if __name__ == "__main__":
    app = MainWindow()
    # export_current_assists()
    app.start_window()
