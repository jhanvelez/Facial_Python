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
git clone https://github.com/tuusuario/facial-app.git
cd facial-app
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
pyinstaller --noconfirm --windowed --onefile main.py
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