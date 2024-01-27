from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        nome = request.form.get("nome")
        idade = request.form.get("idade")
        return f"""
                <script>alert('nome:{nome}, idade:{idade}')
                window.location.href = '/' 
                </script>
        """
    return render_template("index.html")

@app.route("/dados", methods=["POST"])
def dados():
    nome  = request.form.get("nome","?")
    idade = request.form.get("idade","?") 
    apelido  = request.form.get("apelido","?")
    return f"Nome: {nome} - Apelido: {apelido} - Idade: {idade}"

@app.route("/imc", methods=["POST"])
def imc():
    peso  = float(request.form.get("peso","?"))
    altura = float(request.form.get("altura","?")) 
    imc  =     peso /(altura*altura)
    return f"""<h1>IMC - Calculo do Índice de Massa Corporal</h1>
    Peso/(Altura x Altura).=> {peso} / ({altura} * {altura} = {imc} )"""



@app.route("/pessoal", methods=["POST"])
def pessoal():
    return render_template("index.html",nome=nome, idade=idade, apelido=apelido)

@app.route("/info")
def info():
    nome = request.args.get("nome","?")
    idade = request.args.get("idade","?")    
    return f"Nome: {nome}, Idade: {idade}"

@app.route("/entra/<string:nome>/<string:apelido>/<string:lista>")
def entra(nome:str, apelido:str, lista:list):    
    return f"Nome: {nome} - Apelido: {apelido} - Nºs da Sorte: {lista}"

if __name__ == "__main__":
    app.run(debug=True)