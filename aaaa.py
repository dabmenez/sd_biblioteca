from app import app, db
from models import Aluno, Bibliotecario, Livro, Emprestimo

def init_db():
    with app.app_context():
        db.create_all()
        print('Banco de dados inicializado com sucesso!')

if __name__ == '__main__':
    init_db()
