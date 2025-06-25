from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QApplication
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reconocimiento Facial")
        self.showFullScreen()  # Ocupa toda la pantalla

        # Widget para la cámara
        self.camera_label = QLabel()
        self.camera_label.setFixedSize(640, 480)  # Tamaño fijo para la cámara
        self.camera_label.setStyleSheet("background-color: white;")
        self.camera_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # Widget para la información
        self.info_title = QLabel("<b>Información de la persona</b>")
        self.info_title.setAlignment(Qt.AlignLeft)
        self.label_edad = QLabel("Edad: ---")
        self.label_genero = QLabel("Género: ---")
        self.label_expresion = QLabel("Expresión: ---")

        info_layout = QVBoxLayout()
        info_layout.addWidget(self.info_title)
        info_layout.addWidget(self.label_edad)
        info_layout.addWidget(self.label_genero)
        info_layout.addWidget(self.label_expresion)
        info_layout.addStretch()

        # Botón de inicio
        self.button = QPushButton("Iniciar reconocimiento")

        # Layout principal
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.camera_label, alignment=Qt.AlignTop | Qt.AlignLeft)
        top_layout.addLayout(info_layout)

        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(main_layout)
        
        self.status_label = QLabel("")
        main_layout.addWidget(self.status_label, alignment=Qt.AlignCenter)

    def update_frame(self, pixmap: QPixmap):
        self.camera_label.setPixmap(pixmap.scaled(
            self.camera_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def update_info(self, edad=None, genero=None, expresion=None):
        if edad is not None:
            self.label_edad.setText(f"Edad: {edad}")
        if genero is not None:
            self.label_genero.setText(f"Género: {genero}")
        if expresion is not None:
            self.label_expresion.setText(f"Expresión: {expresion}")