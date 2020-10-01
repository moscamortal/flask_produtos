from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask.views import MethodView
from flask.views import View
from models import Produtos

import requests

import json

app = Flask(__name__)
api = Api(app)

#Classes
class Produto(Resource):
    def get(self, id):
        produto = Produtos.query.get(id)
        try :
            response = {
                'id': produto.id,
                'nome': produto.nome,
                'preco': produto.preco,
                'avaliacao_nota': produto.avaliacao_nota
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Produto nao encontrado'
            }
        return response

class ListaProdutos(Resource):
    def get(self):
        produto = Produtos.query.all()
        #if produto:
        response = [{'id':p.id, 'nome':p.nome,'preco':p.preco, 'avaliacao_nota': p.avaliacao_nota} for p in produto]
        return response

    def post(self):
        dados = request.json
        produto = Produtos(nome=dados['nome'], preco=dados['preco'], avaliacao_nota=dados['avaliacao_nota'])
        produto.save()
        response = {
            'id':produto.id,
            'nome': produto.nome,
            'preco': produto.preco,
            'avaliacao_nota': produto.avaliacao_nota
        }
        return response
        #return render_template('index.html', data=data)

api.add_resource(ListaProdutos, '/produto/')
api.add_resource(Produto, '/produto/<int:id>/')
if __name__ == '__main__':
    app.run(debug=True)