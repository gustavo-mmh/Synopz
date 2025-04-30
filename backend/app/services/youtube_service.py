import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import logging

def extract_id_youtube(url):
    youtube_id_match = re.match(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})',
        url)
    return youtube_id_match.group(6) if youtube_id_match else None

def download_subtitle(video_id):
    try:
        ytt_api = YouTubeTranscriptApi()
        transcript_list = ytt_api.list(str(video_id))
        transcript = next(
            (t for t in transcript_list if t.language_code in ['pt', 'en']),
            None
        )
        if not transcript:
            logging.warning(f"Nenhuma legenda encontrada em pt ou en para {video_id}")
            return None
        entries = transcript.fetch()
        return ' '.join([entry.text for entry in entries])

    except (TranscriptsDisabled, NoTranscriptFound) as e:
        logging.warning(f"Legendas não disponíveis para o vídeo {video_id}: {e}")
    except Exception as e:
        logging.exception(f"Erro inesperado ao baixar legenda do vídeo {video_id}: {e}")
    return None
