from app.views.main_window import MainWindow
from app.services.face_service import FaceService

class MainController:
    def __init__(self):
        self.window = MainWindow()
        self.service = FaceService(self.window.update_frame, self.window.update_info)
        self.window.button.clicked.connect(self.iniciar_reconocimiento)

    def show(self):
        self.window.show()

    def iniciar_reconocimiento(self):
        self.window.status_label.setText("Iniciando cámara...")
        self.service.start()