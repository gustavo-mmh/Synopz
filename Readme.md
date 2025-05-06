# Synopz

![GitHub repo size](https://img.shields.io/github/repo-size/gustavo-mmh/Synopz)
![GitHub last commit](https://img.shields.io/github/last-commit/gustavo-mmh/Synopz)
![GitHub stars](https://img.shields.io/github/stars/gustavo-mmh/Synopz?style=social)

## 📌 Sobre o Projeto

O **Synopz** é uma aplicação web full stack composta por backend em Flask e frontend em Angular. Seu objetivo é resumir vídeos do YouTube utilizando a API Gemini do Google AI Studio. O sistema extrai legendas dos vídeos, envia o conteúdo para a IA e retorna um resumo estruturado, facilitando o consumo rápido de informações.

---

## 🏗️ Estrutura do Projeto

- **backend/**: API Flask responsável por processar vídeos, extrair legendas e interagir com a API Gemini.
- **frontend/**: Aplicação Angular que fornece a interface web para o usuário inserir links de vídeos e visualizar os resumos.

---

## 🚀 Como Executar Localmente

### 📋 Pré-requisitos

- Python 3.8+
- Node.js 18+ e npm
- Conta no Google AI Studio com acesso à API Gemini
- Chave de API Gemini

### 🔧 Instalação

#### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/synopz.git
cd synopz
```

#### 2. Backend (Flask)

```bash
cd backend
python -m venv .venv
# Ative o ambiente virtual:
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

pip install -r requirements.txt
```

Opcional: Crie um arquivo `.env` com sua chave de API Gemini:

```
GEMINI_API_KEY=sua_chave_aqui
SECRET_KEY=sua_chave_secreta
```

Inicie o servidor Flask:

```bash
python run.py
```

#### 3. Frontend (Angular)

Abra outro terminal e execute:

```bash
cd frontend
npm install
ng serve
```

Acesse o frontend em [http://localhost:4200](http://localhost:4200).

---

## 🧪 Testes

- **Backend:** Os testes estão na pasta `backend/tests/`. Execute com:
  ```bash
  pytest
  ```
- **Frontend:** Execute testes unitários com:
  ```bash
  ng test
  ```
  Para testes end-to-end:
  ```bash
  ng e2e
  ```

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python, Flask, Google AI Studio API (Gemini)
- **Frontend:** Angular, TailwindCSS

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.
