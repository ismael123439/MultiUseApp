# 🚀 MultiUseApp

Una aplicación web multifuncional desarrollada en Flask que combina tres herramientas útiles en una sola interfaz.

## ✨ Características

- 🎵 **Transcripción y Traducción de Audio**: Convierte archivos de audio a texto y traduce el contenido
- 🖼️ **OCR (Reconocimiento Óptico de Caracteres)**: Extrae texto desde imágenes
- 🌍 **Traductor de Texto**: Traduce texto entre diferentes idiomas

## 🛠️ Tecnologías Utilizadas

- **Flask**: Framework web de Python
- **OpenAI Whisper**: Para transcripción de audio
- **Pytesseract**: Para OCR (reconocimiento de texto en imágenes)
- **Google Translate API**: Para traducción de texto
- **Pillow**: Para procesamiento de imágenes
- **FFmpeg**: Para procesamiento de archivos de audio

## 📋 Requisitos Previos

### Dependencias de Python
```bash
pip install flask pillow pytesseract googletrans==4.0.0-rc1 openai-whisper
```

### Herramientas Externas

#### 1. Tesseract OCR
Necesario para la funcionalidad de OCR.

**Instalación:**
- **Windows**: Descargar desde [GitHub Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- **Linux**: `sudo apt-get install tesseract-ocr`
- **macOS**: `brew install tesseract`

**Configuración:** Actualiza la ruta en `app.py`:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows
```

#### 2. FFmpeg
Necesario para que Whisper pueda procesar archivos de audio.

**Instalación:**
- **Windows**: Descargar desde [ffmpeg.org](https://ffmpeg.org/download.html)
- **Linux**: `sudo apt-get install ffmpeg`
- **macOS**: `brew install ffmpeg`

**Importante**: Asegúrate de que FFmpeg esté en el PATH del sistema.

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/ismael123439/MultiUseApp.git
cd MultiUseApp
```

### 2. Crear entorno virtual (recomendado)
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
*Si no existe `requirements.txt`, instala las dependencias listadas en los requisitos previos.*

### 4. Configurar rutas
Edita `app.py` y configura la ruta de Tesseract según tu sistema operativo.

### 5. Ejecutar la aplicación
```bash
python app.py
```

### 6. Acceder a la aplicación
Abre tu navegador y ve a:
```
http://localhost:5000
```

## 🎯 Funcionalidades

### 🎵 Transcripción y Traducción de Audio
- Sube archivos de audio en formatos compatibles
- Transcribe automáticamente usando Whisper AI
- Traduce el texto transcrito a diferentes idiomas

### 🖼️ OCR - Reconocimiento de Texto en Imágenes
- Sube imágenes con texto
- Extrae automáticamente el texto visible
- Soporte para múltiples idiomas

### 🌍 Traductor de Texto
- Traduce texto entre múltiples idiomas
- Interfaz simple y fácil de usar
- Detección automática del idioma de origen

## 📁 Estructura del Proyecto

```
MultiUseApp/
│
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias Python (si existe)
├── static/               # Archivos estáticos (CSS, JS, imágenes)
├── templates/            # Plantillas HTML
└── uploads/              # Carpeta para archivos subidos (se crea automáticamente)
```

## ⚠️ Solución de Problemas

### Error con Tesseract
- Verifica que Tesseract esté instalado correctamente
- Asegúrate de que la ruta en `app.py` sea correcta
- En Windows, verifica que el ejecutable esté en la ruta especificada

### Error con FFmpeg
- Verifica que FFmpeg esté instalado
- Asegúrate de que esté en el PATH del sistema
- Reinicia la terminal después de la instalación

### Error con dependencias de Python
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Ismael** - [@ismael123439](https://github.com/ismael123439)

## 🙏 Agradecimientos

- OpenAI por Whisper
- Google por Google Translate API
- Tesseract OCR team
- Flask community

---

⭐ Si este proyecto te resulta útil, ¡no olvides darle una estrella!