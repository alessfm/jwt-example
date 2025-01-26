# jwt-example
Atividade da Pós-graduação na UniFAP, um teste com JWT em Flask.

## Requisitos

- [Python ^3.7](https://www.python.org/downloads/)

## Instruções

### Instalar Dependências

_(Opcional)_ Crie um ambiente virtual para instalar as dependências separadamente do seus outros projetos em Python:

  ```bash
  # Windows:
  python -m venv env
  .\env\Scripts\activate

  # Unix:
  python3 -m venv env
  source env/bin/activate
  ```

Agora, realize a instalação das dependências:

  ```bash
  pip install -r requirements.txt

  # Ou manualmente(são duas)
  pip install flask
  pip install pyjwt
  ```

### Executar Projeto

Execute o arquivo `main.py` via terminal ou compilador:
  
  ```bash
  flask --app app run
  # ou
  python -m flask --app app run
  ```

Pronto! A API estará disponível em [localhost:5000](localhost:5000)

## Rotas

1. POST - localhost:5000/login
3. GET - localhost:5000/acesso