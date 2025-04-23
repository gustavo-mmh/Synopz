import logging
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from colorama import Fore
import google.generativeai as genai
from app.services.gemini_service import sum_up_with_gemini
from app.services.youtube_service import extract_id_youtube, download_subtitle

bp_api = Blueprint('api', __name__)
CORS(bp_api)


@bp_api.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        api_key = data.get('api_key', '').strip()
        youtube_url = data.get('youtube_url', '').strip()
        model_name = data.get('model_name', '').strip()

        if not api_key:
            return jsonify({'error': 'API Key não fornecida'}), 400
        if not youtube_url:
            return jsonify({'error': 'URL do YouTube não fornecida'}), 400
        if not model_name:
            return jsonify({'error': 'Modelo não selecionado'}), 400

        genai.configure(api_key=api_key)
        video_id = extract_id_youtube(youtube_url)
        if not video_id:
            return jsonify({'error': 'URL do YouTube inválida'}), 400

        text_caption = download_subtitle(video_id)
        if not text_caption:
            return jsonify({'error': 'Não foi possível baixar a legenda do vídeo'}), 500

        text_caption = text_caption[:10000]
        summary = sum_up_with_gemini(text_caption, api_key, model_name)
        return jsonify({'summary': summary})

    except Exception as e:
        logging.exception("Erro ao resumir vídeo")
        return jsonify({'error': str(e)}), 500


@bp_api.route('/get_models', methods=['POST'])
def get_models():
    try:
        logging.info(Fore.BLUE + 'aqui' + Fore.RESET)
        data = request.get_json()
        api_key = data.get('api_key', '').strip()
        if not api_key:
            logging.info(Fore.RED + 'API Key não fornecida' + Fore.RESET)
            return jsonify({'error': 'API Key não fornecida'}), 400

        genai.configure(api_key=api_key)
        models = [model.name.replace('models/', '') for model in genai.list_models()]
        return jsonify({'models': models})

    except Exception as e:
        logging.info(Fore.BLUE + 'erro' + Fore.RESET)
        return jsonify({'error': str(e)}), 500
