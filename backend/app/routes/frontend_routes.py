from flask import Blueprint, send_from_directory

bp_frontend = Blueprint('frontend', __name__)

@bp_frontend.route('/', defaults={'path': ''})
@bp_frontend.route('/<path:path>')
def serve_frontend(path):
    if path != "" and path is not None:
        return send_from_directory('../frontend/dist/video-ia-summarize-frontend', path)
    else:
        return send_from_directory('../frontend/dist/video-ia-summarize-frontend', 'index.html')
