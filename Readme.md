# Video IA Summarize

![GitHub repo size](https://img.shields.io/github/repo-size/gustavo-mmh/Video_IA_Sumarize)
![GitHub last commit](https://img.shields.io/github/last-commit/gustavo-mmh/Video_IA_Sumarize)
![GitHub stars](https://img.shields.io/github/stars/gustavo-mmh/Video_IA_Sumarize?style=social)

## 📌 Sobre o Projeto

Uma aplicação Flask para resumir vídeos do YouTube utilizando a API do Google AI Studio (Gemini). O projeto extrai legendas de vídeos e gera resumos estruturados com base no conteúdo.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

Certifique-se de ter os seguintes itens instalados:

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Conta no Google AI Studio com acesso à API Gemini
- Chave de API do Google AI Studio

### 🔧 Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/video-ia-summarize.git
    cd video-ia-summarize
   ```	 
2. Crie um ambiente virtual:
    ```bash
    python -m venv .venv
   ```	 
3. Ative o ambiente virtual:
    - No Windows:
    ```bash
    .venv\Scripts\activate
     ```	 
    - No Linux/Mac:
    ```bash
    source .venv/bin/activate
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5. Configure a chave de API no arquivo .env:
    ```bash
    SECRET_KEY=sua_chave_secreta
    ```
6. Inicie o servidor Flask:
    ```bash
    python app.py
    ```
7. Acesse a aplicação no navegador:
    ```bash
    http://127.0.0.1:5000/
    ```
## 📄 Licença
Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.
