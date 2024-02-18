# from flask import Flask, render_template, request
# '''pip install Flask-SQLAlchemy'''
# '''para MSQL -> pip install mysql-connector-python'''
# from flask_sqlalchemy import SQLAlchemy 

# db = SQLAlchemy()
# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ToDoList.db'
# '''app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://usuario:senha@localhost/nome_do_banco'''

# class ToDo(db.Model): 
#     numero = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     nome = db.Column(db.String(100))
#     data = db.Column(db.String(10))
#     descricao = db.Column(db.String(200))

# @app.route("/")
# def index():
#     return render_template("index.html")    

# @app.route("/cadastro")
# def cadastro():
#     return render_template("cadastro.html") 

# '''@app.route("/cadastrar", methods=["POST"])
# def cadastrar():
#     nome  = request.form.get("nome","?")
#     email = request.form.get("email","?") 
#     lista_nomes.append(nome)
#     return """
#         <script>
#             alert('Cadastrado com sucesso!');
#             window.location.href='cadastro.html'
#         </script>
#     """'''


# @app.route("/listar")
# def listar():
#     return render_template("visualizar.html",lista_nomes)   

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ToDoList.db'
# Configuração para suprimir o aviso deprecado
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ToDo(db.Model):
    numero = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    data = db.Column(db.String(10))
    descricao = db.Column(db.String(100))

    def __repr__(self):
        return f'<Usuario {self.nome}>'

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/create_db')
def create_db():
    db.create_all()
    return 'Banco de dados criado!'

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

if __name__ == "__main__":
    app.run(debug=True)