import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_id_youtube(url):
    youtube_id_match = re.match(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})',
        url)
    return youtube_id_match.group(6) if youtube_id_match else None

def download_subtitle(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'en'])
        return ' '.join([entry['text'] for entry in transcript])
    except Exception:
        return None