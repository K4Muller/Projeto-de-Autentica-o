from flask import Flask
from models.user import User
from database import db
#Configuração padrão de um banco de dados sqlalchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = "12345"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)
#Quando a gente abre um banco de dados, quando a gente abre uma conecção com ele, ele cria um conceito chamado:
# Session <- Conexão ativa

#################################################################

@app.route('/')
def hello():
    return 'Olá, mundo!'

if __name__ == "__main__":
    app.run(debug=True)