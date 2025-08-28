# MultiUseApp

¡Bienvenido a **MultiUseApp**! Esta aplicación combina tres funcionalidades principales:

1. 🎵 **Transcripción y Traducción de Audio**  
2. 🖼️ **OCR: Leer texto desde imágenes**  
3. 🌍 **Traductor de Texto**

---

## 📦 Requisitos

Antes de ejecutar la app, asegurate de tener instaladas las siguientes dependencias:

### Dependencias de Python
```bash
pip install flask pillow pytesseract googletrans==4.0.0-rc1 openai-whisper
Herramientas externas
Tesseract OCR: necesario para la lectura de texto en imágenes.
Descarga e instalación
Recordá configurar la ruta en app.py:

python
Copiar código
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
FFmpeg: necesario para que Whisper pueda procesar audios.
Descarga e instalación
Asegurate de que esté en el PATH del sistema para que Whisper lo detecte.

🚀 Cómo correr la app
Clonar el repo:

bash
Copiar código
git clone https://github.com/ismael123439/MultiUseApp.git
cd MultiUseApp
Crear un entorno virtual (opcional pero recomendado):

bash
Copiar código
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
(si no existe requirements.txt, instalá las librerías listadas arriba)

Correr la app:

bash
Copiar código
python app.py
Abrir en el navegador:

arduino
Copiar código
http://localhost:5000