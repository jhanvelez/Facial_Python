# 🧠 Aplicación de Reconocimiento Facial con PySide6 + OpenCV

Esta es una aplicación de escritorio multiplataforma desarrollada en Python que permite detectar rostros en tiempo real y estimar:

- 👤 **Género**
- 🎂 **Edad**
- 😊 **Expresión facial**

La interfaz está hecha con **PySide6**, y se puede ejecutar en **macOS, Windows y Linux**.

---

## 🚀 Requisitos

- Python `3.10.x` o superior (no usar Python 3.13 aún)
- Pip (actualizado)
- OpenCV compatible con DNN
- Cámara web

---

## 🔧 Instalación

1. **Clona el repositorio:**

```bash
git clone git@github.com:jhanvelez/Facial_Python.git
cd Facial_Python
```

2. **Crea un entorno virtual:**

```bash
python3 -m venv env
source env/bin/activate  # En Linux/macOS
env\Scripts\activate     # En Windows
```

3. **Instala los requerimientos:**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## ▶️ Ejecución

```bash
python main.py
```

## 📦 Compilación para distribución

```bash
pyinstaller --noconfirm --onefile --windowed \     
  --add-data "models/gender/gender_deploy.prototxt:models/gender" \
  --add-data "models/gender/gender_net.caffemodel:models/gender" \
  --add-data "models/age/age_deploy.prototxt:models/age" \
  --add-data "models/age/age_net.caffemodel:models/age" \
  --add-data "models/emotion/emotion_model.h5:models/emotion" \
  --add-data "models/haarcascade_frontalface_default.xml:models" \
  main.py
```

---

### ✅ `requirements.txt` correspondiente

Asegúrate de tener este archivo también:

```txt
opencv-python
PySide6
tensorflow~=2.15.0
keras
numpy
