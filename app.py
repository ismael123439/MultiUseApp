import os
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract
import whisper
from googletrans import Translator

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# ---------------- Configuración ---------------- #
BASE_DIR = os.getcwd()
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'temp_uploads')
ALLOWED_AUDIO_EXTENSIONS = {'mp3', 'wav', 'm4a', 'flac', 'ogg', 'aac', 'wma'}
ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp', 'tiff', 'webp'}
MAX_CONTENT_LENGTH = 100 * 1024 * 1024  # 100MB máximo

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------- Inicializar modelos ---------------- #
print("Cargando modelo Whisper...")
whisper_model = whisper.load_model("base")
print("Modelo Whisper cargado exitosamente")

translator = Translator()
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# ---------------- Funciones auxiliares ---------------- #
def allowed_file(filename, filetype='audio'):
    ext = filename.rsplit('.', 1)[1].lower()
    if filetype == 'audio':
        return '.' in filename and ext in ALLOWED_AUDIO_EXTENSIONS
    elif filetype == 'image':
        return '.' in filename and ext in ALLOWED_IMAGE_EXTENSIONS
    return False

def cleanup_temp_file(filepath):
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
            print(f"Archivo temporal eliminado: {filepath}")
    except Exception as e:
        print(f"Error eliminando archivo temporal: {e}")

# ---------------- Rutas ---------------- #
@app.route("/")
def index():
    return render_template("index.html")

# ---------------- Audio → Transcripción + Traducción ---------------- #
@app.route("/audio", methods=["GET"])
def audio_page():
    return render_template("audio.html")

@app.route("/process_audio", methods=["POST"])
def process_audio():
    temp_path = None
    try:
        if 'audio_file' not in request.files:
            return jsonify({'error': 'No se seleccionó ningún archivo'}), 400

        file = request.files['audio_file']
        if file.filename == '':
            return jsonify({'error': 'No se seleccionó ningún archivo'}), 400
        if not allowed_file(file.filename, 'audio'):
            return jsonify({'error': 'Formato de audio no soportado'}), 400

        filename = secure_filename(file.filename)
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(temp_path)

        source_language = request.form.get('source_language', 'auto')
        target_language = request.form.get('target_language', 'es')

        if source_language != "auto":
            result = whisper_model.transcribe(temp_path, language=source_language)
        else:
            result = whisper_model.transcribe(temp_path)

        transcription = result.get("text", "").strip()
        detected_lang = result.get("language", source_language)

        if source_language == "auto":
            translation = translator.translate(transcription, dest=target_language)
        else:
            translation = translator.translate(transcription, src=source_language, dest=target_language)

        translated_text = translation.text

        return jsonify({
            'success': True,
            'transcription': transcription,
            'translation': translated_text,
            'source_language': detected_lang,
            'target_language': target_language
        })
    except Exception as e:
        return jsonify({'error': f'Error procesando el audio: {str(e)}'}), 500
    finally:
        if temp_path:
            cleanup_temp_file(temp_path)

# ---------------- OCR ---------------- #
@app.route("/ocr", methods=["GET"])
def ocr_page():
    return render_template("ocr.html")

@app.route("/process_ocr", methods=["POST"])
def process_ocr():
    temp_path = None
    try:
        if 'image_file' not in request.files:
            return jsonify({'error': 'No se seleccionó ninguna imagen'}), 400

        file = request.files['image_file']
        if file.filename == '':
            return jsonify({'error': 'No se seleccionó ninguna imagen'}), 400
        if not allowed_file(file.filename, 'image'):
            return jsonify({'error': 'Formato de imagen no soportado'}), 400

        filename = secure_filename(file.filename)
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(temp_path)

        image = Image.open(temp_path)
        text = pytesseract.image_to_string(image)

        return jsonify({'success': True, 'text': text})
    except Exception as e:
        return jsonify({'error': f'Error procesando la imagen: {str(e)}'}), 500
    finally:
        if temp_path:
            cleanup_temp_file(temp_path)

# ---------------- Traductor de texto ---------------- #
@app.route("/translate", methods=["GET"])
def translate_page():
    return render_template("translate.html")

@app.route("/process_translate", methods=["POST"])
def process_translate():
    try:
        text = request.form.get('text', '')
        lang = request.form.get('lang', 'es')
        if not text:
            return jsonify({'error': 'No se ingresó texto'}), 400

        translated = translator.translate(text, dest=lang).text
        return jsonify({'success': True, 'translated': translated})
    except Exception as e:
        return jsonify({'error': f'Error traduciendo el texto: {str(e)}'}), 500

# ---------------- Health check ---------------- #
@app.route("/health")
def health_check():
    return jsonify({'status': 'OK', 'whisper_loaded': whisper_model is not None})

# ---------------- Run ---------------- #
if __name__ == "__main__":
    print("Iniciando aplicación Flask unificada...")
    print("Formatos de audio soportados:", ', '.join(ALLOWED_AUDIO_EXTENSIONS))
    print("Formatos de imagen soportados:", ', '.join(ALLOWED_IMAGE_EXTENSIONS))
    app.run(debug=True, host='0.0.0.0', port=5000)
