# Usar uma imagem oficial do Python como base
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de requisitos e instalar as dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar o código Python para o contêiner
COPY app.py app.py

# Copiar o diretório de template
COPY template/ template/

# Expor a porta 5000 para acesso externo
EXPOSE 5000

# Comando para executar o script Python
CMD ["python", "app.py"]
