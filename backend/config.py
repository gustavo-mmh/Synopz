import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sua_chave_secreta_aqui')
    DEBUG = os.environ.get('DEBUG', True)
    TESTING = os.environ.get('TESTING', False)
    # Adicione outras configurações conforme necessário