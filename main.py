from flask import Flask, jsonify, request
from functools import wraps
import datetime
import jwt

CHAVE = "123456"
ALGORITMO = "HS256"
usuarios = [
  {
    "id": 1,
    "nome": "Alessandro FM",
    "email": "alessandrofm@example.com",
    "senha": "Admin1234",
    "cargo": "ADMIN"
  },
  {
    "id": 2,
    "nome": "Jonathan",
    "email": "jonh@example.com",
    "senha": "teste4567",
    "cargo": "USER"
  }
]

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
  body = request.get_json()
  usuario = next((u for u in usuarios if u["email"] == body["email"]), None)
  
  if not usuario:
    return jsonify({"mensagem": "Usuário não encontrado"}), 404
  
  if usuario["senha"] != body["senha"]:
    return jsonify({"mensagem": "Email ou Senha incorretos"}), 401

  return gerar_token(usuario)
  

def gerar_token(usuario):
  PAYLOAD = {
    "id": usuario["id"], 
    "usuario": usuario["nome"], 
    "cargo": usuario["cargo"],
    "iat": datetime.datetime.now(),
    "exp": datetime.datetime.now() + datetime.timedelta(hours=12)
  }

  token = jwt.encode(PAYLOAD, CHAVE, ALGORITMO)

  return jsonify({"mensagem": "Usuário validado", "token": token})


def validar_token(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    token = request.authorization.token
    
    if not token:
      return jsonify({"mensagem": "Token não enviado"}), 401
    
    try:
      data = jwt.decode(token, CHAVE, [ALGORITMO])
    except:
      return jsonify({"mensagem": "Token inválido/expirado"}), 401
    
    return f(data["usuario"], *args, **kwargs)
  return decorated


@app.route("/acesso", methods=["GET"])
@validar_token
def acessar(nomeUsuario):
  return jsonify({"mensagem": f"Bem-vindo {nomeUsuario}"}), 201


if __name__ == '__main__':
  app.run()