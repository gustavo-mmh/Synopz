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

def test_summarize_missing_transcript_text(client):
    response = client.post('/summarize', json={
        'api_key': 'fake-key',
        'model_name': 'gemini-pro'
    })
    assert response.status_code == 400
    json_data = response.get_json()
    assert 'error' in json_data
    assert json_data['error'] == 'Texto da transcrição não fornecido'

def test_summarize_success(client):
    with patch('google.generativeai.configure'), \
         patch('app.routes.api_routes.sum_up_with_gemini', return_value='resumo gerado') as mock_sum_up:
        response = client.post('/summarize', json={
            'api_key': 'fake-key',
            'transcript_text': 'this is a test transcript',
            'model_name': 'gemini-pro'
        })
        assert response.status_code == 200
        data = response.get_json()
        assert 'summary' in data
        assert data['summary'] == 'resumo gerado'
        mock_sum_up.assert_called_once_with('this is a test transcript', 'fake-key', 'gemini-pro')
