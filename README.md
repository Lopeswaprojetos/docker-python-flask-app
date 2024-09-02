# Aplicativo Flask Dockerizado

Este projeto demonstra um aplicativo web simples usando Flask, rodando dentro de contêineres Docker. É projetado como uma introdução básica ao uso do Docker com aplicações Python Flask.

## Funcionalidades
- Um aplicativo Flask básico com uma página de saudação simples.
- Dockerfile para containerizar a aplicação.
- Docker Compose para configuração fácil de múltiplos contêineres.
- Exemplo de tratamento de logs e templates no Flask.

## Estrutura do Projeto
```plaintext
docker-python-flask-app/
│
├── app.py                  # Aplicação principal em Flask
├── docker-compose.yml      # Arquivo Docker Compose para definir os serviços
├── Dockerfile              # Dockerfile para construir o contêiner da aplicação Flask
├── dockerignore            # Especifica arquivos a serem ignorados ao construir a imagem Docker
├── logs/                   # Diretório para armazenar logs da aplicação
├── requirements.txt        # Dependências do Python
├── templates/              # Templates HTML para o aplicativo Flask
└── test_app.py             # Testes unitários básicos para a aplicação


Getting Started
Prerequisites
Docker installed on your system
Docker Compose installed

Running the Application
Clone the repository:
git clone https://github.com/Lopeswaprojetos/docker-python-flask-app.git
cd docker-python-flask-app

Build and start the containers:
docker-compose up --build

Access the web application at http://localhost:5000

Testing the Application
You can run the included unit tests with the following command:
docker-compose run web pytest

Contributing
Feel free to submit pull requests or open issues to improve the project.
