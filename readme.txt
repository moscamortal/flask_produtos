Rotas:
http://127.0.0.1:5000/produto/

----------
Rota /produto/
Retorna a lista dos produtos,
----------
Rota /produto/id
Retorna os dados de um produto especifico.
----------
Banco de dados em SQLite em anexo 'database'
Tentei colocar uma view para apresentar os dados e permitir pesquisar, porém não consegui.

Acabei utilizando somente o API RESTfull do flask para retornar os dados do banco de dados.

Tabela produtos,
id, nome, preco e avalicao_nota.