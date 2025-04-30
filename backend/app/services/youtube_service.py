import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import logging
from colorama import Fore

def extract_id_youtube(url):
    youtube_id_match = re.match(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})',
        url)
    return youtube_id_match.group(6) if youtube_id_match else None

def download_subtitle(video_id):
    try:
        ytt_api = YouTubeTranscriptApi()
        logging.info(Fore.BLUE + f"Resumindo vídeo {video_id}" + Fore.RESET)
        transcript_list = ytt_api.list(video_id)
        transcript = next(
            (t for t in transcript_list if t.language_code in ['pt', 'en']),
            None
        )
        if not transcript:
            logging.info(Fore.BLUE +f"Nenhuma legenda encontrada em pt ou en para {video_id}" + Fore.RESET)
            return None, f"Nenhuma legenda encontrada em pt ou en para {video_id}"
        entries = transcript.fetch()
        text = ' '.join([entry.text for entry in entries])
        return text, None

    except (TranscriptsDisabled, NoTranscriptFound) as e:
        logging.info(Fore.BLUE +f"Legendas não disponíveis para o vídeo {video_id}: {e}" + Fore.RESET)
        return None, f"Legendas não disponíveis para o vídeo {video_id}"
    except Exception as e:
        logging.info(Fore.BLUE +f"Erro inesperado ao baixar legenda do vídeo {video_id}: {e}" + Fore.RESET)
    return None, f"Erro inesperado ao baixar legenda do vídeo {video_id}"
