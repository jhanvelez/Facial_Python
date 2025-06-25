from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QTimer, QUrl
from PySide6.QtGui import QPixmap
import json
from pathlib import Path

class AdWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.label = QLabel("Publicidad")
        self.label.setScaledContents(True)
        self.video = QVideoWidget()
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setAudioOutput(self.audio)
        self.player.setVideoOutput(self.video)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.video)
        self.ads = []
        self.index = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.show_next)
        self.timer.start(10000)  # cada 10 segundos

        self.load_ads()
        self.show_next()

    def load_ads(self):
        config_path = Path("config/ads_config.json")
        if config_path.exists():
            with open(config_path, "r") as f:
                self.ads = json.load(f)

    def show_next(self):
        if not self.ads:
            return

        ad = self.ads[self.index]
        file_path = f"assets/ads/{ad['filename']}"

        if ad["type"] == "image":
            self.player.stop()
            self.video.hide()
            self.label.show()
            self.label.setPixmap(QPixmap(file_path))
        elif ad["type"] == "video":
            self.label.hide()
            self.video.show()
            self.player.setSource(QUrl.fromLocalFile(file_path))
            self.player.play()

        self.index = (self.index + 1) % len(self.ads)
