from flask import Flask, render_template

app = Flask(__name__)


# Página inicial
@app.route("/")
def inicio():
    return render_template("index.html")


# Sobre a KBSistemas
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


# Serviços (sistemas, sites, aplicativos)
@app.route("/servicos")
def servicos():
    return render_template("servicos.html")


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


if __name__ == "__main__":
    app.run(debug=True)
