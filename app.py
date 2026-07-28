from flask import Flask, render_template
import os

app = Flask(__name__)


# Página inicial
@app.route("/")
def inicio():
    return render_template("index.html")


# Sobre a KBSistemas
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


# Serviços
@app.route("/servicos")
def servicos():
    return render_template("servicos.html")


# Projetos
@app.route("/projetos")
def projetos():
    return render_template("projetos.html")


# Planos e soluções
@app.route("/planos")
def planos():
    return render_template("planos.html")


# Contato
@app.route("/contato")
def contato():
    return render_template("contato.html")


# Orçamento
@app.route("/orcamento")
def orcamento():
    return render_template("orcamento.html")


# Teste de funcionamento
@app.route("/ping")
def ping():
    return "ok"


if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=porta)
