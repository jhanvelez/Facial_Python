import cv2
import os
import numpy as np
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

class FaceService:
    def __init__(self, update_frame, update_info):
        self.update_frame = update_frame
        self.update_info = update_info
        self.video = cv2.VideoCapture(0)

        if not self.video.isOpened():
            print("❌ No se pudo abrir la cámara")

        self.timer = QTimer()
        self.timer.timeout.connect(self.process_frame)

        base = os.path.dirname(os.path.abspath(__file__))

        # Cargar modelos de género y edad
        gender_proto = os.path.join(base, "../../models/gender/gender_deploy.prototxt")
        gender_model = os.path.join(base, "../../models/gender/gender_net.caffemodel")
        self.gender_net = cv2.dnn.readNetFromCaffe(gender_proto, gender_model)
        self.gender_list = ['Male', 'Female']

        age_proto = os.path.join(base, "../../models/age/age_deploy.prototxt")
        age_model = os.path.join(base, "../../models/age/age_net.caffemodel")
        self.age_net = cv2.dnn.readNetFromCaffe(age_proto, age_model)
        self.age_list = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

        # Modelo de emociones (Keras)
        emotion_model_path = os.path.join(base, "../../models/emotion/emotion_model.h5")
        self.emotion_net = load_model(emotion_model_path, compile=False)
        self.emotion_list = ['Enojado', 'Disgustado', 'Asustado', 'Feliz', 'Triste', 'Sorprendido', 'Neutral']

        # Detector de rostro
        haar_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        self.face_detector = cv2.CascadeClassifier(haar_path)

    def start(self):
        self.timer.start(30)

    def stop(self):
        self.timer.stop()
        self.video.release()

    def process_frame(self):
        ret, frame = self.video.read()
        if not ret:
            self.update_info("❌ No se pudo leer la cámara")
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        genero = "Desconocido"
        edad = "?"
        emocion = "?"

        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]
            blob = cv2.dnn.blobFromImage(face_img, 1.0, (227, 227),
                                        (78.4263, 87.7689, 114.8958), swapRB=False)

            # Género
            self.gender_net.setInput(blob)
            genero = self.gender_list[self.gender_net.forward()[0].argmax()]

            # Edad
            self.age_net.setInput(blob)
            edad = self.age_list[self.age_net.forward()[0].argmax()]

            # Emoción
            face_gray = gray[y:y+h, x:x+w]
            try:
                face_gray = cv2.resize(face_gray, (64, 64))
                face_gray = face_gray.astype("float") / 255.0
                face_gray = np.expand_dims(face_gray, axis=-1)
                face_gray = np.expand_dims(face_gray, axis=0)
                pred = self.emotion_net.predict(face_gray, verbose=0)[0]
                emocion = self.emotion_list[pred.argmax()]
            except Exception as e:
                print("❌ Error en emoción:", e)

            # Dibujar resultados
            text = f"{genero}, {edad}, {emocion}"
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

            break

        self.update_info(edad=edad, genero=genero, expresion=emocion)

        # Mostrar en GUI
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qimage = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        self.update_frame(pixmap)
