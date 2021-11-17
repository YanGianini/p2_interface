from flask import Flask, render_template, redirect
from application import app
from application.model.dao.produtodao import ProdutoDao

produtoDao = ProdutoDao()
lista_produto = produtoDao.listar_produtos()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/produtos")
def produto():
    return render_template("produtos.html", lista_produto=lista_produto[0:4])