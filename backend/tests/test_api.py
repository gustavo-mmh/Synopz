import pytest
from flask import Flask
from app.app import create_app
from unittest.mock import patch

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_models_missing_api_key(client):
    response = client.post('/get_models', json={})
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_get_models_success(client):
    with patch('google.generativeai.list_models') as mock_list_models:
        mock_list_models.return_value = [type('Model', (), {'name': 'models/gemini-pro'})()]
        response = client.post('/get_models', json={'api_key': 'fake-key'})
        assert response.status_code == 200
        data = response.get_json()
        assert 'models' in data
        assert 'gemini-pro' in data['models']

def test_summarize_missing_fields(client):
    response = client.post('/summarize', json={})
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_summarize_invalid_youtube_url(client):
    with patch('google.generativeai.configure'), \
         patch('app.services.youtube_service.extract_id_youtube', return_value=None):
        response = client.post('/summarize', json={
            'api_key': 'fake-key',
            'youtube_url': 'invalid',
            'model_name': 'gemini-pro'
        })
        assert response.status_code == 400
        assert 'error' in response.get_json()

def test_summarize_success(client):
    with patch('google.generativeai.configure'), \
         patch('backend.app.services.youtube_service.extract_id_youtube', return_value='123'), \
         patch('backend.app.services.youtube_service.download_subtitle', return_value=('texto da legenda', None)), \
         patch('backend.app.services.gemini_service.sum_up_with_gemini', return_value='resumo gerado'):
        response = client.post('/summarize', json={
            'api_key': 'fake-key',
            'youtube_url': 'https://youtube.com/watch?v=123',
            'model_name': 'gemini-pro'
        })
        assert response.status_code == 200
        data = response.get_json()
        assert 'summary' in data
        assert data['summary'] == 'resumo gerado'
