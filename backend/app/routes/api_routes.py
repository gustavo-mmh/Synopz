import logging
from flask import Blueprint, request, jsonify
from flask_cors import CORS
from colorama import Fore
import google.generativeai as genai
from app.services.gemini_service import sum_up_with_gemini
logging.basicConfig(filename='', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
bp_api = Blueprint('api', __name__)
CORS(bp_api)


@bp_api.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        api_key = data.get('api_key', '').strip()
        transcript_text = data.get('transcript_text', '').strip()
        model_name = data.get('model_name', '').strip()

        if not api_key:
            return jsonify({'error': 'API Key não fornecida'}), 400
        if not transcript_text:
            return jsonify({'error': 'Texto da transcrição não fornecido'}), 400
        if not model_name:
            return jsonify({'error': 'Modelo não selecionado'}), 400

        genai.configure(api_key=api_key)

        logging.info(Fore.BLUE + "Resumindo texto" + Fore.RESET)
        transcript_text = transcript_text[:10000]
        summary = sum_up_with_gemini(transcript_text, api_key, model_name)
        return jsonify({'summary': summary})

    except Exception as e:
        logging.exception("Erro ao resumir vídeo: %s", str(e))
        return jsonify({'error': str(e)}), 500


@bp_api.route('/get_models', methods=['POST'])
def get_models():
    try:
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
