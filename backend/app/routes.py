import logging

from colorama import Fore
from flask import Blueprint, render_template, request,jsonify, send_from_directory
from flask_cors import CORS
from app.services.gemini_service import sum_up_with_gemini
from app.services.youtube_service import extract_id_youtube, download_subtitle
import google.generativeai as genai
logging.basicConfig(filename='', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
bp = Blueprint('main', __name__)

CORS(bp)  # Permite requisições de outros domínios
@bp.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    url = ""
    error = ""
    models = []

    try:
        api_key = request.form.get('api_key', '').strip()
        if api_key:
            genai.configure(api_key=api_key)
            models = [model.name for model in genai.list_models()]
            logging.info(Fore.BLUE + str(models) + Fore.RESET)
    except Exception as e:
        error = f"Erro ao carregar modelos: {str(e)}"
        logging.info(Fore.RED + error + Fore.RESET)

    if request.method == 'POST' and not error:
        url = request.form.get('youtube_url', '').strip()
        model_name = request.form.get('model_name', '').strip()

        if not api_key:
            error = "Por favor, insira a API Key do Google AI Studio"
            logging.info(Fore.RED + error + Fore.RESET)
        elif not url:
            error = "Por favor, insira a URL do YouTube"
            logging.info(Fore.RED + error + Fore.RESET)
        elif not model_name:
            error = "Por favor, selecione um modelo"
            logging.info(Fore.RED + error + Fore.RESET)
        else:
            video_id = extract_id_youtube(url)
            if not video_id:
                error = "URL do YouTube inválida"
                logging.info(Fore.RED + error + Fore.RESET)
            else:
                text_caption = download_subtitle(video_id)
                if not text_caption:
                    error = "Não foi possível baixar a legenda do vídeo"
                    logging.info(Fore.RED + error + Fore.RESET)
                else:
                    text_caption = text_caption[:10000]
                    summary = sum_up_with_gemini(text_caption, api_key, model_name)

    return render_template('index.html', summary=summary, url=url, error=error, models=models)

@bp.route('/get_models', methods=['POST'])
def get_models():
    try:
        data = request.get_json()
        api_key = data.get('api_key', '').strip()
        if not api_key:
            logging.info(Fore.RED + 'API Key não fornecida' + Fore.RESET)
            return jsonify({'error': 'API Key não fornecida'}), 400

        genai.configure(api_key=api_key)
        # Remove o prefixo 'models/' dos nomes dos modelos
        models = [model.name.replace('models/', '') for model in genai.list_models()]
        return jsonify({'models': models})
    except Exception as e:
        logging.info(Fore.RED + str(e) + Fore.RESET)
        return jsonify({'error': str(e)}), 500
    
    bp.route('/<path:path>', methods=['GET'])
def serve_frontend(path):
    return send_from_directory('../frontend/dist/video-ia-summarize-frontend', path)

@bp.route('/', methods=['GET'])
def serve_index():
    return send_from_directory('../frontend/dist/video-ia-summarize-frontend', 'index.html')