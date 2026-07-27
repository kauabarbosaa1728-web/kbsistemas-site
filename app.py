from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route("/")
def inicio():
    return render_template("index.html")

# Sobre
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

# Serviços
@app.route("/servicos")
def servicos():
    return render_template("servicos.html")

# Planos
@app.route("/planos")
def planos():
    return render_template("planos.html")

# Contato
@app.route("/contato")
def contato():
    return render_template("contato.html")


if __name__ == "__main__":
    app.run(debug=True)
