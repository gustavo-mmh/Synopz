from flask import Blueprint, render_template, request

from app.services.gemini_service import sum_up_with_gemini
from app.services.youtube_service import extract_id_youtube, download_subtitle

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    url = ""
    error = ""

    if request.method == 'POST':
        api_key = request.form.get('api_key', '').strip()
        url = request.form.get('youtube_url', '').strip()

        if not api_key:
            error = "Por favor, insira a API Key do Google AI Studio"
        elif not url:
            error = "Por favor, insira a URL do YouTube"
        else:
            video_id = extract_id_youtube(url)
            if not video_id:
                error = "URL do YouTube inválida"
            else:
                text_caption = download_subtitle(video_id)
                if not text_caption:
                    error = "Não foi possível baixar a legenda do vídeo"
                else:
                    text_caption = text_caption[:10000]
                    summary = sum_up_with_gemini(text_caption, api_key)

    return render_template('index.html', summary=summary, url=url, error=error)